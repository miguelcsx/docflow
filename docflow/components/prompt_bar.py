# docflow/components/prompt_bar.py

import reflex as rx
from docflow.state import State
from docflow.style.prompt_bar_style import prompt_bar_style
from docflow.components.loading_icon import loading_icon

def prompt_bar() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.chakra.form(
                rx.chakra.form_control(
                    rx.hstack(
                        rx.radix.text_field.root(
                            rx.radix.text_field.input(
                                placeholder="Enter additional information... (optional)",
                                id="prompt",
                                width=["15em", "20em", "45em", "50em", "50em", "50em"],
                                on_change=State.set_prompt,
                            ),
                            rx.radix.text_field.slot(
                                rx.tooltip(
                                    rx.icon(tag="info", size=14),
                                    content="Enter additional information for the documentation.",
                                    variant="soft",
                                )
                            ),
                        ),
                        rx.button(
                            rx.cond(
                                State.processing,
                                loading_icon(height="1em"),
                                rx.text("Generate")
                            ),
                            type="submit",
                        ),
                        align_items="center",
                    ),
                    is_disabled=State.processing,
                ),
                on_submit=State.process_documentation,
                reset_on_submit=True,
            ),
        ),
        style=prompt_bar_style,
    )
