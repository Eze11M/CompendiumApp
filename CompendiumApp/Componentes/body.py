import reflex as rx
from CompendiumApp.Estados.general import GlobalState

lorem_ipsum: str = """
Lorem ipsum dolor sit amet consectetur adipiscing, elit platea ultricies justo eros. Rhoncus porttitor habitasse lobortis parturient elementum bibendum pharetra venenatis lacus fermentum, donec phasellus vivamus condimentum suscipit posuere ligula eleifend vulputate a fusce, magnis metus nibh et ut porta malesuada tempus molestie. Mattis ad risus hac faucibus eu egestas elementum ornare fermentum donec, id libero lectus quis gravida suspendisse vulputate etiam.

Ligula dui scelerisque venenatis egestas vehicula neque himenaeos tristique senectus velit dictum magna auctor ad, penatibus cum posuere aenean morbi netus blandit condimentum consequat sociosqu rhoncus ut. Ante nunc habitasse tellus integer nostra nullam ligula accumsan libero condimentum, fusce non a hendrerit egestas sollicitudin mattis varius leo sem, erat at taciti lobortis dis suspendisse imperdiet lacus et. Odio nunc curabitur natoque leo fermentum lacinia pretium, inceptos eget cum ligula magnis neque taciti ultrices, turpis integer etiam phasellus venenatis aptent.
"""

def imagen_presentacion(imagen: str) -> rx.Component:
    return rx.center(
        rx.text("COMPENDIUM"),
        rx.text("Todo el contenido, mismo lugar."),
        direction="column",
        border_width="thick",
        padding="10px",
        width="100%",
        height="30em",
        background=f"center/cover url('{imagen}')"
    )

def imagen_ilustrativa(imagen: str) -> rx.Component:
    return rx.box(
        rx.image(
            imagen,
            width="20em",
            height="auto"
        )
    )

def seccion_texto(titulo: str, contenido: str) -> rx.Component:
    return rx.box(
        rx.text(titulo, size="4"),
        rx.text(contenido, size="2"),
        width="40%"
    )

def body() -> rx.Component:
    return rx.center(
        rx.vstack(
            imagen_presentacion(GlobalState.imagen_background),
            rx.hstack(
                imagen_ilustrativa(GlobalState.imagen_background),
                seccion_texto("TITULO", lorem_ipsum),
                border_width="thick",
                width="100%",
                height="auto",
                align="center",
                justify="center",
                spacing="9"
            ),
            rx.hstack(
                seccion_texto("TITULO", lorem_ipsum),
                imagen_ilustrativa(GlobalState.imagen_background),
                border_width="thick",
                width="100%",
                align="center",
                justify="center",
                spacing="9"
            ),
            align="center",
            width="80%",
            spacing="7"
        ),
        border_width="thick",
        border_color="sky",
        padding="10px",
        height="auto",
        width="100%"
    )