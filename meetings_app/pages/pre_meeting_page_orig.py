import reflex as rx
from .pre_meeting_state import PreReuniaoState
from .sidebar import sidebar


def pre_meeting_page_orig() -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.divider(orientation="vertical"),
        main(),
        direction="row",
        height="100vh",
        width="100vw",
    )


def main():
    return rx.container(
        rx.vstack(
            rx.heading("Criar Reunião"),
            rx.input(placeholder="Nome da Reunião", on_change=PreReuniaoState.set_nome),
            rx.text_area(placeholder="Propósito", on_change=PreReuniaoState.set_proposito),
            rx.input(placeholder="Periodicidade", on_change=PreReuniaoState.set_periodicidade),
            rx.input(placeholder="Participantes (separados por vírgula)", on_change=lambda v: PreReuniaoState.set_participantes(v.split(","))),
            
            rx.divider(),
            rx.heading("Itens a serem discutidos"),
            rx.input(placeholder="Descrição do Item", on_change=PreReuniaoState.set_novo_item),
            rx.input(placeholder="Responsável", on_change=PreReuniaoState.set_responsavel),
            rx.select(
                ["Texto", "Número", "Anexo"],
                value=PreReuniaoState.tipo_dado,
                on_change=PreReuniaoState.set_tipo_dado,
            ),
            rx.button("Adicionar Item", on_click=PreReuniaoState.adicionar_item),
            
            rx.vstack(
                rx.foreach(PreReuniaoState.itens, lambda item: 
                    rx.text(f"{item['descricao']} - {item['responsavel']} ({item['tipo_dado']})")
                )
            ),
            
            rx.divider(),
            rx.button("Salvar Reunião", on_click=PreReuniaoState.salvar_reuniao, color_scheme="blue"),
        ),
        padding="20px",
        max_width="600px",
        margin="auto"
    )
