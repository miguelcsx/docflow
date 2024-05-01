# docflow/style/prompt_bar_style.py

import reflex as rx

prompt_bar_style = {
    "position": "sticky",
    "bottom": "0",
    "left": "0",
    "padding": "16px",
    "backdrop_filter": "auto",
    "backdrop_blur": "lg",
    "border_top": f"1px solid {rx.color('mauve', 3)}",
    "background_color": rx.color("mauve", 2),
    "align_items": "stretch",
    "width": "100%",
}