# docflow/docflow.py

import reflex as rx
from docflow.state import State
from docflow.components import (
    navbar,
    text_box,
    prompt_bar,
)
from docflow.style.index_style import (
    document_style,
    index_style,
)

def values() -> rx.Component:
    return rx.container(
    )


def index() -> rx.Component:
    return rx.chakra.vstack(
        navbar.navbar(),
        rx.center(
            text_box.text_box(),
            text_box.formated_box(),
            style=document_style,
        ),
        prompt_bar.prompt_bar(),
        style=index_style,
    )

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="indigo",
    )
)
app.add_page(index)
