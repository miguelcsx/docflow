# docflow/docflow.py

import reflex as rx
from docflow.state import State
from docflow.components import (
    navbar,
    text_box,
)


def values() -> rx.Component:
    return rx.container(
    )


def index() -> rx.Component:
    return rx.chakra.vstack(
        navbar.navbar(),
        text_box.text_box(),
        backgroud_color=rx.color("mauve", 1),
        color=rx.color("mauve", 11),
        min_height="100vh",
        align_items="stretch",
        spacing="0",
    )

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="indigo",
    )
)
app.add_page(index)
