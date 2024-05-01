# docflow/state.py

import reflex as rx

class State(rx.State):
    """The app state."""

    # Code input
    code: str = ""

    # Model input
    model: str = ""

    # API token input
    token: str = ""

    # Processing state
    processing: bool = False

    # Documentation output
    documentation: str = ""

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

    def handle_submit(self, form_data: dict):
        self.settings_data = form_data

    async def process_documentation(self, form_data: dict[str, str]):
        form_data["code"] = self.code
        self.form_data = form_data
        self.documentation = form_data["code"] + form_data["prompt"]
        
