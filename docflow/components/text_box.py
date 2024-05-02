# docflow/components/text_box.py

import reflex as rx
from docflow.state import State
from docflow.style.text_box_style import (
    text_box_style,
    formated_box_style,
)


def text_box() -> rx.Component:
    return rx.box(
        rx.text_area(
            value=State.code,
            placeholder="Enter your code here...",
            on_change=State.set_code,
            style=text_box_style,
        ),
    )


def formated_box() -> rx.Component:
    return rx.box(
        rx.scroll_area(
            rx.markdown(
                State.documentation,
            ),
            style=formated_box_style,
        )
    )


