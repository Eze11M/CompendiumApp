import reflex as rx
from CompendiumApp.Paginas.index import index
from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


app = rx.App()
app.add_page(index)
