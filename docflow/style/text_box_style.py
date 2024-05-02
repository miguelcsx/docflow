# docflow/style/text_box_style.py

import reflex as rx

text_box_style = {
    "margin": "0.5em",
    "min_width": "35em",
    "min_height": "75vh",
    "max_height": "80vh",
    "font_family": "monospace",
    "white_space": "pre-wrap",
    "color": rx.color("mauve", 11),
    "border": f"1px solid {rx.color('mauve', 2)}",
    "background_color": rx.color("mauve", 1),
}

scroll_formated_style = {
    "padding": "0.5em",
    "padding_x": "1.5em",
    "min_width": "35em",
    "max_width": "40em",
    "min_height": "75vh",
    "max_height": "75vh",

}

formated_box_style = {
    "margin": "0.5em",
    "border": f"1px solid {rx.color('mauve', 12)}",
    "background_color": rx.color("mauve", 1),
}

copy_style = {
    "right": "0",
    "bottom": "0"
}