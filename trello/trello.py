import flet


class TrelloApp:
    def __init__(self, page: flet.Page):
        self.page = page
        self.appbar_items = [
            flet.PopupMenuItem(text="login"),
            flet.PopupMenuItem(), #divider
            flet.PopupMenuItem(text="settings")
        ]
        self.appbar = flet.AppBar(
            leading= flet.Icon(flet.icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width= 100,
            title= flet.Text("Trello", size=32, text_align="start"),
            center_title=0,
            toolbar_height=75,
            bgcolor= flet.colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                flet.Container(
                    content= flet.PopupMenuButton(
                        items= self.appbar_items
                    ),
                    margin= flet.margin.only(left=50, right=25)
                )
            ]
        )
        self.page.appbar = self.appbar
        self.page.update()