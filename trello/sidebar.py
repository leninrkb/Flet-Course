import flet 

class Sidebar(flet.UserControl):
    def __init__(self, app_layout, page):
        self.page = page
        self.top_nav_items = [
            flet.NavigationRailDestination(
                label_content= "Boards",
                label= "Boards",
                icon= flet.icons.BOOK_OUTLINED
            ),
            flet.NavigationRailDestination(
                label_content= "Members",
                label= "Members",
                icon= flet.icons.PERSON
            )
        ]
        self.top_nav_rail = flet.NavigationRail(
            selected_index= None,
            label_type= "all",
            on_change= self.top_nav_items,
            bgcolor= flet.colors.BLUE_GREY,
            extended= True,
            expand= True
        )
        
        def build(self):
            self.view = flet.Container(
            content= flet.Column([
                flet.Row([
                    flet.Text("Workspace"),
                ]),
                # divider
                flet.Container(
                    bgcolor= flet.colors.BLACK26,
                    border_radius= flet.border_radius.all(30),
                    height=1,
                    alignment= flet.alignment.center_right,
                    width=220
                ),
                self.top_nav_rail,
                # divider
                flet.Container(
                    bgcolor= flet.colors.BLACK26,
                    border_radius= flet.border_radius.all(30),
                    height=1,
                    alignment= flet.alignment.center_right,
                    width=220
                ),
                ], tight=True),
                padding= flet.padding.all(15),
                margin= flet.margin.all(0),
                width=250,
                bgcolor= flet.colors.BLUE_GREY,
                )
            return self.view
        
        def top_nav_change(self, e):
            self.top_nav_rail.selected_index = e.control.selected_index
            self.update()