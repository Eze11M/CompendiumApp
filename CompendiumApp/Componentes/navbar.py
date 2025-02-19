import reflex as rx
from CompendiumApp.Estados.general import GlobalState

def isologo_box(logo: str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.image(
                src=logo,
                width="35px",
                height="auto",
                border_radius="100px 100px",
                border="5px solid #555",
            ),
            rx.text("COMPENDIUM"),
            align="center"
        ),
        border_width="thick",
        padding="10px"
    )

def boton(texto: str) -> rx.Component:
    return rx.button(
        texto,
        background_color="#F5F5DC",
        color="black"
    )

def botones_box() -> rx.Component:
    return rx.box(
        rx.hstack(
            boton("Boton 1"),
            boton("Boton 2"),
            boton("Boton 3"),
            justify="center"
        ),
        border_width="thick",
        padding="10px"
    )

def navbar() -> rx.Component:
    return rx.box(
        rx.hstack(
            isologo_box(GlobalState.logo),
            botones_box(),
            align="baseline",
            justify="between"
        ),
        border_width="thick",
        padding="10px",
        width="100%",
        position="fixed",
        top="0px",
        z_index="5"
    )