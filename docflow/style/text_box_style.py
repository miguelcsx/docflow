# docflow/style/text_box_style.py

import reflex as rx

text_box_style = {
    "margin": "0.5em",
    "width": "40em",
    "height": "30em",
    "font_family": "monospace",
    "white_space": "pre-wrap",
    "color": rx.color("mauve", 11),
    "border": f"1px solid {rx.color('mauve', 2)}",
    "background_color": rx.color("mauve", 1),
}

formated_box_style = {
    "padding": "0.5em",
    "margin": "0.5em",
    "width": "40em",
    "height": "30em",
    "border": f"1px solid {rx.color('mauve', 12)}",
    "background_color": rx.color("mauve", 1),
}
