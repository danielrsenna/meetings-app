import reflex as rx


def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color="#000000"),
            rx.text(
                text, size="4", 
                color="#000000",
                font_weight="regular",
                #font_family= "Garamond",
            ),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("gray", 4),
                    "color": rx.color("gray", 11),
                },
                "border-radius": "1em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Início", "house", "/"),
        sidebar_item("Guia de Reuniões", "book-text", "/guia-reunioes"),
        sidebar_item("Nova Reunião", "file-plus-2", "/nova-reuniao/step1"),
        sidebar_item("Reuniões", "file-text", "/em-construcao"),
        spacing="1",
        width="100%",
    )


def sidebar() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.vstack(
                rx.link(
                    rx.image(
                        src="/minerva-foods-logo2.png",
                        width="6em",
                        height="auto",
                    ),
                    href='/',
                ),
                rx.link(
                    rx.heading(
                        "Gestão de Reuniões",
                        size="4",
                        weight="bold",
                        #font_family= "Garamond",
                        color="#000000",
                    ),
                    href='/', 
                    underline="none",
                ),
                align="start",
                justify="start",
                padding_x="0.5rem",
                width="100%",
            ),
            sidebar_items(),
            rx.spacer(),
            rx.vstack(
                rx.vstack(
                    sidebar_item(
                        "Configurações", "settings", "/em-construcao"
                    ),
                    sidebar_item(
                        "Sair", "log-out", "/"
                    ),
                    spacing="1",
                    width="100%",
                ),
                rx.divider(),
                rx.hstack(
                    rx.image(
                        src="/fabian_profile.jpg",
                        width="2.5em",
                        height="auto",
                        border_radius="100%",
                    ),
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "Fabian Meyer",
                                size="3",
                                weight="bold",
                            ),
                            rx.text(
                                "@fabian.meyer",
                                size="2",
                                weight="medium",
                            ),
                            width="100%",
                        ),
                        spacing="0",
                        align="start",
                        justify="start",
                        width="100%",
                    ),
                    padding_x="0.5rem",
                    align="center",
                    justify="start",
                    width="100%",
                ),
                width="100%",
                spacing="5",
            ),
            spacing="5",
            padding_x="1em",
            padding_y="1.5em",
            bg=rx.color("gray", 3),
            align="start",
            height="100vh",
            width="16em",
        ),
    )
