import reflex as rx

from . import pages
from . import navigation

app = rx.App(
    theme=rx.theme(
        #appearance="light", 
        # has_background=True, 
        # panel_background="solid",
        scaling="90%",
        #radius="medium",   
        #accent_color="bronze",
    )
)

#Website Pages
app.add_page(pages.pre_meeting_page_pt1, navigation.routes.NEW_MEETING_pt1, title="Nova Reunião")  
app.add_page(pages.pre_meeting_page_pt2, navigation.routes.NEW_MEETING_pt2, title="Nova Reunião")  
app.add_page(pages.pre_meeting_page_pt3, navigation.routes.NEW_MEETING_pt3, title="Nova Reunião")  
app.add_page(pages.pre_meeting_page_orig, navigation.routes.NEW_MEETING, title="Nova Reunião")  
app.add_page(pages.homepage, navigation.routes.HOME, title="Início")  
app.add_page(pages.guia_page, navigation.routes.GUIA, title="Guia Reuniões")  
app.add_page(pages.errorpage, navigation.routes.ERROR, title="Em Construção")