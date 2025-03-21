import reflex as rx
from .pre_meeting_state import PreReuniaoState
from .sidebar import sidebar


def pre_meeting_page_pt2() -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.divider(orientation="vertical"),
        main(),
        direction="row",
        height="100vh",
        width="100vw",
    )

def inputs() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("Como (Inputs)", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Define a forma ou os métodos pelos quais os dados e informações serão inseridos na reunião.", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Descreva os canais e ferramentas que serão utilizados. Ex.: dashboards, relatórios, apresentações, formulários online; \n- Explique o processo para a coleta dos inputs. Ex.: via email, sistemas colaborativos, reuniões preparatórias; \n- Inclua prazos para o envio dos materiais e os formatos esperados."),
                direction="column",
            ),
            rx.text_area(placeholder="Digite os Inputs da reunião"),
            direction="column",
            height="95%",
            justify="between",
        ),
        height="50vh",
        width="98%",
        border="1px solid #000",
    )

def de_quem() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("De Quem", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Identifica as fontes de onde os inputs virão, ou seja, quem é o responsável por fornecer cada informação ou dado que servirá de base para as discussões.", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Liste os responsáveis ou departamentos que devem fornecer os dados. Ex.: financeiro, operações, marketing; \n- Especifique as responsabilidades individuais ou coletivas; \n- Garanta que os responsáveis estejam cientes dos prazos e do conteúdo esperado."),
                direction="column",
            ),
            rx.text_area(placeholder="Digite de Quem virão os inputs da reunião"),
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
                inputs(),
                de_quem(),               
                rx.flex(          
                    rx.link(
                        rx.button(
                            "Voltar", 
                            color_scheme="blue"
                        ), 
                        href="/nova-reuniao/step1",
                        is_external=False,
                    ),
                    rx.link(
                        rx.button(
                            "Continuar", 
                            color_scheme="blue"
                        ), 
                        href="/nova-reuniao/step3",
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
