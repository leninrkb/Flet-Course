import flet
from trello import  TrelloApp

def main(page: flet.Page):
    page.title = "Trello"
    app = TrelloApp(page)
    page.add(app)
    page.update()
    
flet.app(target=main)