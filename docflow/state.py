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

    def set_code(self, code: str):
        """Set the code input."""
        self.code = code

    def set_model(self, model: str):
        """Set the model input."""
        self.model = model

    def set_token(self, token: str):
        """Set the API token input."""
        self.token = token