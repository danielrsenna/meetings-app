import reflex as rx

def errorpage() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Página em Construção..", size="9"),
            rx.text(
                "O app ainda está em desenvolvimento, contamos com sua compreensão.",
                size="5",
            ),
            rx.link(
                rx.button("Voltar"),
                href="/guia-reunioes",
                is_external=False,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )