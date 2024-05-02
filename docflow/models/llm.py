# docflow/models/google_ai.py

from langchain.prompts import PromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

def get_model(token, model, temperature=0.0):
    match model:
        case "anthropic":
            llm = ChatAnthropic(api_key=token, model="claude-3-sonnet-20240229", temperature=temperature)
        case "gemini":
            llm = ChatGoogleGenerativeAI(google_api_key=token, model="gemini-pro", temperature=temperature)
        case "openai":
            llm = ChatOpenAI(api_key=token, model="gpt-3.5-turbo", temperature=temperature)
    return llm

def test_api_token(token, model) -> bool:
    try:
        llm = get_model(token, model)
        llm.invoke("")
    except Exception:
        return False
    return True


def generate_markdown(token, model, text, instructions):
    llm = get_model(token, model)

    function_prompt_template: str = """
    Generate markdown documentation for the given code and apply extra instructions:
    code: {text}
    extra instructions: {instructions}
    """

    prompt: str = PromptTemplate.from_template(template=function_prompt_template)
    prompt_formatted_str: str = prompt.format(
        text= text, instructions= instructions
    )

    result = llm.invoke(prompt_formatted_str)

    return result.content


def generate_docstring(token, model, text, instructions):
    llm = get_model(token, model)

    function_prompt_template: str = """
    Generate docstring documentation for the given code and apply extra instructions using the provided documentation style:
    code: {text}
    extra instructions: {instructions}
    documentation style: {documentation_style}
    """

    documentation_style: str = 'Numpy-Style'

    prompt: str = PromptTemplate.from_template(template=function_prompt_template)
    prompt_formatted_str: str = prompt.format(
        text= text,
        instructions= instructions,
        documentation_style= documentation_style,
    )

    result = llm.invoke(prompt_formatted_str)

    return result.content