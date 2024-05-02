# docflow/components/text_box.py

import reflex as rx
from docflow.state import State
from docflow.style.text_box_style import (
    copy_style,
    text_box_style,
    formated_box_style,
    scroll_formated_style
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
    return rx.hstack(
        rx.scroll_area(
            rx.markdown(
                State.documentation,
            ),
            style=scroll_formated_style
        ),
        rx.button(
            rx.icon(tag="copy", size=18, color=rx.color("mauve", 9)),
            on_click=rx.set_clipboard(State.documentation),
            background="transparent",
            _hover = {
                "opacity": 0.5,
                "cursor": "pointer",
                "background": "transparent",
            },
            _active = {
                "size": "0.8em",
                "transform": "scale(0.8)",
            },
            style = copy_style,
        ),
        style=formated_box_style,
    )
