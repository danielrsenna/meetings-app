import reflex as rx
from .pre_meeting_state import PreReuniaoState
from .sidebar import sidebar


def pre_meeting_page_pt3() -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.divider(orientation="vertical"),
        main(),
        direction="row",
        height="100vh",
        width="100vw",
    )

def outputs() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("Outputs", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Define os resultados esperados da reunião, ou seja, os outputs que deverão ser gerados a partir do encontro.", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Especifique os produtos tangíveis. Ex.: decisões estratégicas, planos de ação, documentos, relatórios de acompanhamento; \n- Detalhe os indicadores de sucesso ou os critérios para avaliação dos outputs; \n- Seja claro quanto às metas a serem alcançadas ao final da reunião."),
                direction="column",
            ),
            rx.text_area(placeholder="Digite os Outputs da reunião"),
            direction="column",
            height="95%",
            justify="between",
        ),
        height="50vh",
        width="98%",
        border="1px solid #000",
    )

def para_quem() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("Para Quem/Para Que", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Explica quem são os destinatários dos outputs e qual o propósito final das decisões e ações geradas.", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Indique os stakeholders ou áreas beneficiadas com os outputs. Ex.: alta administração, equipes operacionais, investidores; \n- Explique como esses resultados contribuirão para a estratégia ou melhoria dos processos. Ex.: facilitar a execução de projetos, melhorar a comunicação interna, acelerar decisões; \n- Relacione os outputs aos objetivos estratégicos da organização, demonstrando seu impacto."),
                direction="column",
            ),
            rx.text_area(placeholder="Descreva quem utilizará os outputs e para qual finalidade"),
            direction="column",
            height="95%",
            justify="between",
        ),
        height="50vh",
        width="98%",
        border="1px solid #000",
    )


def main() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.heading("Parametrização da Reunião", as_="h2"),
            rx.text("Defina os parâmetros da sua reunião antes de começar. Essas informações serão usadas durante e após a mesma.", size="3"),
            align="start",
            justify="start",
            direction="column",
            width="95%",
        ),
        rx.scroll_area(
            rx.flex(
                outputs(),
                para_quem(),               
                rx.flex(          
                    rx.link(
                        rx.button(
                            "Voltar", 
                            color_scheme="blue"
                        ), 
                        href="/nova-reuniao/step2",
                        is_external=False,
                    ),
                    rx.link(
                        rx.button(
                            "Enviar", 
                            color_scheme="grass"
                        ), 
                        href="/",
                        is_external=False,
                    ),
                    spacing="3",
                ),
                direction="column",
                align="center",
                #padding="2em",
                width="100%",
                spacing="5",
            ),
            type="hover",
            scrollbars="vertical",
            height="95%",
            width="90%",
        ),
        direction="column",
        height="100%",
        width="100%",
        align="center",
        padding_top="2em",
        padding_bottom="2em",
        spacing="6",
    )




# def main():
#     return rx.container(
#         rx.vstack(
#             rx.heading("Criar Reunião"),
#             rx.input(placeholder="Nome da Reunião", on_change=PreReuniaoState.set_nome),
#             rx.text_area(placeholder="Propósito", on_change=PreReuniaoState.set_proposito),
#             rx.input(placeholder="Periodicidade", on_change=PreReuniaoState.set_periodicidade),
#             rx.input(placeholder="Participantes (separados por vírgula)", on_change=lambda v: PreReuniaoState.set_participantes(v.split(","))),
            
#             rx.divider(),
#             rx.heading("Itens a serem discutidos"),
#             rx.input(placeholder="Descrição do Item", on_change=PreReuniaoState.set_novo_item),
#             rx.input(placeholder="Responsável", on_change=PreReuniaoState.set_responsavel),
#             rx.select(
#                 ["Texto", "Número", "Anexo"],
#                 value=PreReuniaoState.tipo_dado,
#                 on_change=PreReuniaoState.set_tipo_dado,
#             ),
#             rx.button("Adicionar Item", on_click=PreReuniaoState.adicionar_item),
            
#             rx.vstack(
#                 rx.foreach(PreReuniaoState.itens, lambda item: 
#                     rx.text(f"{item['descricao']} - {item['responsavel']} ({item['tipo_dado']})")
#                 )
#             ),
            
#             rx.divider(),
#             rx.button("Salvar Reunião", on_click=PreReuniaoState.salvar_reuniao, color_scheme="blue"),
#         ),
#         padding="20px",
#         max_width="600px",
#         margin="auto"
#     )
