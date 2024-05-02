# docflow/components/navbar.py

import reflex as rx
from docflow.components.model_select import model_select
from docflow.state import (
    State,
    Mode
)
from docflow.style.navbar_style import (
    navbar_style,
    sidebar_style,
)

def sidebar(trigger) -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(trigger),
        rx.drawer.overlay(),
        rx.drawer.portal(
            rx.drawer.content(
                rx.vstack(
                    rx.heading("DocFlow", color=rx.color("mauve", 11)),
                    rx.divider(),
                    model_select(),
                    width = "80%",
                ),
                style= sidebar_style,
            )
        ),
        direction="left",
    )

def navbar() -> rx.Component:
    modes = ["markdown", "docstring"]
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.heading("DocFlow"),
                rx.badge(
                    rx.tooltip(
                        rx.icon(
                            tag="info",
                            size=14,
                        ),
                        content=f"You are using {State.model} model",
                        variant="soft",
                    ),
                ),
                align_items="center",
            ),
            rx.hstack(
                rx.color_mode.icon(),
                rx.color_mode.switch(),
                rx.select.root(
                    rx.select.trigger(),
                    rx.select.content(
                        rx.select.group(
                            rx.select.label("Select a functionality"),
                            *[rx.select.item(
                                mode.title(),
                                value=mode
                            )
                            for mode in modes],
                        ),
                    ),
                    default_value=modes[0],
                    on_change=State.set_mode,
                ),
                sidebar(
                    rx.button(
                        rx.icon(
                            tag="sliders-horizontal",
                            color=rx.color("mauve", 11),
                        ),
                        background_color=rx.color("mauve", 6),
                    )
                ),
                align_items="center",
            ),
            justify="between",
            align_items="center",
        ),
        style=navbar_style,
    )