# docflow/style/navbar_style.py

import reflex as rx

sidebar_style = {
    "top": "auto",
    "right": "auto",
    "height": "100%",
    "width": "20em",
    "padding": "2em",
    "background_color": rx.color("mauve", 2),
    "outline": "none",
}

navbar_style = {
    "backdrop_filter": "auto",
    "backdrop_blur": "lg",
    "padding": "12px",
    "border_bottom": f"1px solid {rx.color('mauve', 2)}",
    "background_color": rx.color("mauve", 1),
    "position": "sticky",
    "top": "0",
    "z_index": "100",
    "align_items": "center",
}