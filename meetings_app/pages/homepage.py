import reflex as rx

def homepage() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Bem-vindo(a)!", size="9"),
            rx.text(
                "Comece criando uma reunião!",
                size="5",
            ),
            rx.link(
                rx.button("Criar Reunião"),
                href="/guia-reunioes",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )