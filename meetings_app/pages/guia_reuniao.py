import reflex as rx
from .sidebar import sidebar


def guia_page() -> rx.Component:
    return rx.flex(
        sidebar(),
        rx.divider(orientation="vertical"),
        main(),
        direction="row",
        height="100vh",
        width="100vw",
    )

def main() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.heading("Guia Prático para Reuniões Eficientes", as_="h2"),
            rx.text("Estrutura, regras e boas práticas para reuniões produtivas", size="3"),
            direction="column",
            padding_left="2em",
            padding_top="2em",
        ),
        rx.flex(
            card_antes_reuniao(),
            card_durante_reuniao(),
            card_depois_reuniao(),
            direction="row",
            align="center",
            padding_left="2em",
            padding_right="2em",
            #width="100%",
            spacing="3",
            justify="between",
        ),
        direction="column",
        height="95vh",
        #padding="2em",
        spacing="3",
    )

def card_antes_reuniao() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.heading("1. Antes da Reunião", size="3"),
            rx.flex(
                guideline_item(
                    "Defina o propósito e objetivos SMART",
                    "Regra: Só faça a reunião se for realmente necessária e tenha um objetivo claro.",
                    "Dica: Se um e-mail resolver, cancele a reunião. Use objetivos específicos e mensuráveis."
                ),
                guideline_item(
                    "Convide apenas quem é essencial",
                    "Regra: Evite reuniões lotadas. Quanto mais gente, menos eficiência.",
                    "Dica: Inclua apenas decisores e quem tem informações críticas."
                ),
                guideline_item(
                    "Prepare a pauta e compartilhe materiais",
                    "Regra: Reuniões sem pauta se tornam longas e improdutivas.",
                    "Dica: Liste os tópicos, defina o tempo para cada um e envie com antecedência."
                ),
                guideline_item(
                    "Confirme disponibilidade e envie convite",
                    "Regra: Garanta que as pessoas certas possam participar no horário adequado.",
                    "Dica: Verifique agendas antes de marcar e envie lembretes."
                ),
                direction="column",
                spacing="3",
                justify="center",
            ),
            align="center",
            direction="column",
            spacing="3",
            justify="between",
        ),
        border="1px solid #000",
        width="32%",
        height="100%",
    )

def card_durante_reuniao() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.heading("2. Durante a Reunião", size="3"),
            rx.flex(
                guideline_item(
                    "Comece e termine no horário",
                    "Regra: Respeite o tempo de todos. Atrasos e prolongamentos quebram a produtividade.",
                    "Dica: Estabeleça tempos curtos e objetivos para cada tema."
                ),
                guideline_item(
                    "Mantenha o foco e evite distrações",
                    "Regra: Sem conversas paralelas, sem celulares e sem desvios da pauta.",
                    "Dica: Nomeie um facilitador para manter a discussão alinhada."
                ),
                guideline_item(
                    "Incentive a participação ativa",
                    "Regra: Se alguém está na reunião, é porque deve contribuir.",
                    "Dica:  Pergunte diretamente a quem está calado e evite monopolizar a conversa."
                ),
                guideline_item(
                    "Tome decisões claras e atribua responsáveis",
                    "Regra: Reuniões sem decisões e responsáveis são desperdício de tempo.",
                    "Dica: Para cada decisão, defina o dono da ação e o prazo de entrega."
                ),
                direction="column",
                spacing="3",
                justify="center",
            ),
            align="center",
            direction="column",
            spacing="3",
            justify="between",
        ),
        border="1px solid #000",
        width="32%",
        height="100%",
    )

def card_depois_reuniao() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.heading("3. Após a Reunião", size="3"),
            rx.flex(
                guideline_item(
                    "Registre as decisões e tarefas (ata)",
                    "Regra: Se não foi registrado, não existiu.",
                    "Dica: Faça um resumo com decisões, responsáveis e prazos."
                ),
                guideline_item(
                    "Envie a ata e garanta entendimento",
                    "Regra: Todos devem saber o que foi decidido e o que devem fazer.",
                    "Dica: Mantenha o documento curto e objetivo para fácil leitura."
                ),
                guideline_item(
                    "Acompanhe prazos e responsabilidades",
                    "Regra: O que não é cobrado, não é entregue.",
                    "Dica: Use ferramentas como planilhas ou software de gestão para monitoramento."
                ),
                guideline_item(
                    "Analise métricas e implemente melhorias",
                    "Regra: Sempre há como tornar as reuniões mais produtivas.",
                    "Dica: Meça duração, decisões tomadas e execução das tarefas para ajustes futuros."
                ),
                direction="column",
                spacing="3",
                justify="center",
                align="stretch",
            ),
            align="center",
            direction="column",
            spacing="3",
            justify="between",
        ),
        border="1px solid #000",
        width="32%",
        height="100%",
    )

def guideline_item(title: str, rule: str, tip: str) -> rx.Component:
    return rx.flex(
        rx.text(f"{title}", font_weight="bold"),
        rx.text(f"➡ {rule}"),
        rx.text(f"💡 {tip}", font_style="italic"),
        direction="column",
        align="start",
        justify="start",
        spacing="2",
    )