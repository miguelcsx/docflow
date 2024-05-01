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
    documentation: str = "# Hello World"


    def set_code(self, code: str):
        """Set the code input."""
        self.code = code

    def set_model(self, model: str):
        """Set the model input."""
        self.model = model

    def set_token(self, token: str):
        """Set the API token input."""
        self.token = token

    async def process_documentation(self, form_data: dict[str, str]):
        # code = form_data["code"]

        # if code == "":
        return
        
