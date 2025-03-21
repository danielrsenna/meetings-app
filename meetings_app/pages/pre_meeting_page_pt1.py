import reflex as rx
from .pre_meeting_state import PreReuniaoState
from .sidebar import sidebar


def pre_meeting_page_pt1() -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.divider(orientation="vertical"),
        main(),
        direction="row",
        height="100vh",
        width="100vw",
    )

def titulo() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("Título da Reunião", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Defina um título/nome para a sua reunião", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Nome claro e autoexplicativo; \n- Seja conciso e direto; \n- xxxxxxxxx"),
                direction="column",
            ),
            rx.text_area(placeholder="Digite o Título da reunião", on_blur=PreReuniaoState.set_nome),
            direction="column",
            height="95%",
            justify="between",
        ),
        height="50vh",
        width="98%",
        border="1px solid #000",
    )

def proposito() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("Propósito da Reunião e Objetivos", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Defina claramente o objetivo principal do encontro. Este campo deve responder à pergunta: Por que estamos nos reunindo? ", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Especifique o tema ou a problemática a ser tratada. Ex.: Alinhamento estratégico, revisão de metas, tomada de decisão, resolução de problemas; \n- Seja conciso e direto, evitando termos vagos; \n- Indique como o propósito da reunião se conecta aos objetivos estratégicos da empresa."),
                direction="column",
            ),
            rx.text_area(placeholder="Digite o Propósito da reunião", on_blur=PreReuniaoState.set_proposito),
            direction="column",
            height="95%",
            justify="between",
        ),
        height="50vh",
        width="98%",
        border="1px solid #000",
    )
    
def quando() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("Quando", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Determine a data, horário e periodicidade da reunião. Este campo organiza o 'quando' a reunião ocorrerá.", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Defina a data e o horário específicos ou a frequência (diária, semanal, mensal, etc); \n- Considere o tempo necessário para a pauta e o tempo disponível dos participantes; \n- Avalie se há períodos do dia mais produtivos para reuniões estratégicas."),
                direction="column",
            ),
            rx.text_area(placeholder="Digite o Quando da reunião", on_blur=PreReuniaoState.set_periodicidade),
            direction="column",
            height="95%",
            justify="between",
        ),
        height="50vh",
        width="98%",
        border="1px solid #000",
    )

def participantes() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.flex(
                rx.heading("Quem Participa", as_="h2"),
                align="center",
                justify="center",
            ),
            rx.divider(orientation="horizontal"),
            rx.flex(
                rx.text("Descrição:", size="3", weight="bold"),
                rx.text("Liste os participantes essenciais da reunião, definindo os papéis de cada um. Ex.: dono da reunião, moderador, participantes estratégicos, prestadores de serviço.", size="3", weight="light"),
                direction="column",
            ),
            rx.flex(
                rx.text("Dicas de Preenchimento:", size="3", weight="bold"),
                rx.markdown("- Inclua os decisores e os responsáveis diretos pelos temas abordados; \n- Evite sobrecarregar a reunião com participantes que não contribuirão para a pauta; \n- Considere a necessidade de incluir especialistas ou consultores externos, se aplicável."),
                direction="column",
            ),
            rx.flex(
                rx.input(
                    placeholder="Digite o nome do participante",
                    value=PreReuniaoState.novo_participante,
                    on_change=PreReuniaoState.set_novo_participante,
                ),
                rx.button(
                    "Adicionar Participante",
                    on_click=PreReuniaoState.add_participante,
                    color_scheme="blue",
                ),
                direction="row",
                align="center",
                margin_top="10px",
            ),
            rx.flex(
                rx.foreach(
                    PreReuniaoState.participantes,
                    lambda p: rx.text(f"- {p['nome']}")
                ),
                direction="column",
                margin_top="10px",
            ),
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
                titulo(),
                proposito(),
                quando(),
                participantes(),          
                rx.link(
                    rx.button(
                        "Continuar", 
                        color_scheme="blue",
                    ), 
                    href="/nova-reuniao/step2",
                    is_external=False,
                ),
                direction="column",
                align="center",
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
