import reflex as rx
from CompendiumApp.Componentes.navbar import navbar
from CompendiumApp.Componentes.footer import footer

def index() -> rx.Component:
    return rx.center(
        navbar(),
        footer(),
        border_width="thick",
        padding="10px",
        border_color="tomato",
        height="100%",
        width="auto"
    )