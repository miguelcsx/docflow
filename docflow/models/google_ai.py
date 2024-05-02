# docflow/models/google_ai.py

from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def test_api_token(token) -> bool:
    try:
        llm = ChatGoogleGenerativeAI(google_api_key=token, model="gemini-pro")
        print(llm)
        llm.invoke("")
    except Exception:
        return False
    return True


def generate_markdown(token, text, instructions):
    llm = ChatGoogleGenerativeAI(
        google_api_key=token,
        model="gemini-pro",
        temperature=0,
    )

    function_prompt_template: str = """
    Generate markdown documentation for the given code and apply extra instructions.
    code: {text}
    extra instructions: {instructions}
    """

    prompt: str = PromptTemplate.from_template(template=function_prompt_template)
    prompt_formatted_str: str = prompt.format(
        text= text, instructions= instructions
    )

    result = llm.invoke(prompt_formatted_str)

    return result.content
