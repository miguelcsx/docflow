# docflow/components/text_box.py

import reflex as rx
from docflow.state import State
from docflow.style.text_box_style import text_box_style

def text_box() -> rx.Component:
    return rx.vstack(
        rx.text_area(
            value=State.code,
            placeholder="Enter your code here...",
            on_change=State.set_code,
            rows="20",
            style=text_box_style,
        ),
    )
