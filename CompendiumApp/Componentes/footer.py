import reflex as rx
from CompendiumApp.Estados.general import GlobalState

def link_contacto(texto: str, url: str, icono: str) -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.icon(icono),
            rx.link(texto, href=url),
            rx.icon("link")
        ),
    )

def contacto_box(icono: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src=icono,
                width="100px",
                height="auto",
                border_radius="100px 100px",
                border="5px solid #555",
            ),
            rx.vstack(
                link_contacto("Link 1", "/", "hexagon"),
                link_contacto("Link 2", "/", "hexagon"),
                link_contacto("Link 3", "/", "hexagon"),
                link_contacto("Link 4", "/", "hexagon"),
                link_contacto("Link 5", "/", "hexagon")
            ),
            align="center",
            spacing="7"
        ),
        border_width="thick",
        padding="5px"
    )

def credito_link(texto: str, url: str) -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.link(texto, href=url),
            rx.icon("heart-handshake")
        ),
    )

def creditos_box(icono: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src=icono,
                width="100px",
                height="auto",
                border_radius="100px 100px",
                border="5px solid #555",
            ),
            rx.vstack(
                credito_link("Credito 1", "/"),
                credito_link("Credito 2", "/"),
                credito_link("Credito 3", "/"),
                credito_link("Credito 4", "/")
            ),
            align="center",
            spacing="7"
        ),
        border_width="thick",
        padding="5px",
    )

def made_with_reflex_box(icono: str) -> rx.Component:
    return rx.box(
        rx.center(
            rx.link("Powered by Reflex", href="https://reflex.dev/"),
            rx.image(
                src=icono,
                width="35px",
                height="auto",
                border_radius="100px 100px",
                border="5px solid #555",
            ),
            spacing="3"
        ),
        border_width="thick",
        padding="10px",
        width="100%",
    )

def footer() -> rx.Component:
    return rx.box(
            rx.vstack(
                rx.center(
                    contacto_box(GlobalState.icono_conexion),
                    rx.spacer(),
                    creditos_box(GlobalState.icono_conexion),
                    border_width="thick",
                    padding="10px",
                    width="70%"
                ),
                made_with_reflex_box(GlobalState.icono_reflex),
                width="100%",
                align="center"
            ),
        border_width="thick",
        padding="10px",
        width="100%",
    )