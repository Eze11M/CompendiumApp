import reflex as rx
from CompendiumApp.Componentes.navbar import navbar
from CompendiumApp.Componentes.footer import footer
from CompendiumApp.Componentes.body import body

def index() -> rx.Component:
    return rx.center(
        navbar(),
        body(),
        footer(),
        direction="column",      
        border_width="thick",
        padding="10px",
        border_color="tomato",
        height="100%",
        width="auto"
    )