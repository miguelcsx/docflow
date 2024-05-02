# docflow/state.py

import reflex as rx
from docflow.models.google_ai import (
    test_api_token,
    generate_markdown,
)

class State(rx.State):
    """The app state."""

    # Code input
    code: str = ""

    # Model input
    model: str = ""

    # API token input
    token: str = ""

    prompt: str = ""

    # Documentation output
    documentation: str = ""

    # Processing state
    loading: bool = False
    processing: bool = False

    settings_data: dict = {}

    form_data: dict = {}

    def set_code(self, code: str):
        """Set the code input."""
        self.code = code

    def set_model(self, model: str):
        """Set the model input."""
        self.model = model

    def set_token(self, token: str):
        """Set the API token input."""
        self.token = token

    def set_prompt(self, prompt: str):
        self.prompt = prompt

    def handle_submit(self, settings_data: dict):
        self.loading = True
        yield
        if not test_api_token(self.token):
            self.loading = False
            print("Invalid api token")
            return
        self.settings_data = settings_data
        self.loading = False

    def process_documentation(self, form_data: dict[str, str]):
        self.form_data = form_data
        
        if self.settings_data['token'] == "":
            return
        
        if self.code == "":
            return
        
        self.processing = True
        yield
        
        self.documentation = generate_markdown(self.token, self.code, self.prompt)

        self.processing = False
