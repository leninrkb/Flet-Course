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
            pass