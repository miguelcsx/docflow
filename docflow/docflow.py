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
        rx.tablet_and_desktop(
        rx.center(
            text_box.text_box(),
            text_box.formated_box(),
            style=document_style,
        ),
        ),
        rx.mobile_only(
            rx.flex(
                text_box.text_box(),
                text_box.formated_box(),
                width="100%",
                direction="column",
            )
        ),
          
        prompt_bar.prompt_bar(),
        style=index_style,
    )

app = rx.App(
    theme=rx.theme(
        appearance="light",
        accent_color="indigo",
        has_background=True,
        radius="medium",
        
    )
)
app.add_page(index)
