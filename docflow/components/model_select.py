# docflow/components/model_select.py

import reflex as rx
from enum import Enum
from docflow.state import (
    State,
    Model
)
from docflow.components.loading_icon import loading_icon


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
                        ),
                    ),
                    default_value=models[0].lower().replace(" ", ""),
                    name="model",
                ),
                rx.input(
                    name="token",
                    value=State.token,
                    placeholder="Enter your API token here...",
                    on_change=State.set_token,
                    type="password",
                    required=True,
                ),
                rx.button(
                    rx.cond(
                        State.loading,
                        loading_icon(height="1em"),
                        rx.text("Submit"),
                    ),
                    type="submit",
                ),
            ),
            on_submit=State.handle_submit,
            reset_on_submit=True,
        ),
    )
