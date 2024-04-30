# docflow/components/model_select.py

import reflex as rx
from docflow.state import State
from enum import Enum

class ModelSelectState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data

class Model(Enum):
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    OPENAI = "openai"

def model_select() -> rx.Component:
    models = [model.value for model in Model]
    return rx.vstack(
        rx.form.root(
            rx.vstack(
                rx.select.root(
                    rx.select.trigger(),
                    rx.select.content(
                        rx.select.group(
                            rx.select.label("Select a model"),
                            *[rx.select.item(
                                    model.title().replace("_", " "),
                                    value=model,
                                ) 
                                for model in models],
                        )
                    ),
                    default_value=models[0].lower().replace(" ", ""),
                    name="model",
                ),
                rx.input(
                    name="token",
                    default_value=State.token,
                    value=State.token,
                    placeholder="Enter your API token here...",
                    on_change=State.set_token,
                    type="password",
                    required=True,
                ),
                rx.button(
                    "Submit",
                    type="submit",
                ),
            ),
            on_submit=ModelSelectState.handle_submit,
            reset_on_submit=True,
        ),
        rx.divider(size="4"),
        rx.heading("Results"),
        rx.text(ModelSelectState.form_data.to_string()),
        width="100%",
        direction="column",
        spacing="2",
    )
