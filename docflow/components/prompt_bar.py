# docflow/components/prompt_bar.py

import reflex as rx
from docflow.state import State
from docflow.style.prompt_bar_style import prompt_bar_style

class LoadingIcon(rx.Component):
    library = "react-loading-icons"
    tag = "SpinningCircles"
    stroke: rx.Var[str]
    stroke_opacity: rx.Var[str]
    fill: rx.Var[str]
    fill_opacity: rx.Var[str]
    stroke_width: rx.Var[str]
    speed: rx.Var[str]
    height: rx.Var[str]

    def get_event_triggers(self) -> dict:
        return {"on_change": lambda status: [status]}

loading_icon = LoadingIcon.create


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
            )
        ),
        style=prompt_bar_style,
    )
