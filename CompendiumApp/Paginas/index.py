import reflex as rx
from CompendiumApp.Componentes.navbar import navbar

def index() -> rx.Component:
    return rx.container(
        navbar()
    )