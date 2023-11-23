import flet
from sidebar import Sidebar

class AppLayout(flet.Row):
    def __init__(self, app, page:flet.Page, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        self.toggle_nav_rail_button = flet.IconButton(
            icon= flet.icons.ARROW_CIRCLE_RIGHT,
            on_click= self.toggle_nav_rail
        )
        self.sidebar = Sidebar(self, page)
        self._active_view:flet.Control = flet.Column(
            controls=[
                flet.Text("active view")
            ],
            alignment= "center",
            horizontal_alignment= "center"
        )
        self.controls = [
            self.sidebar, 
            self.toggle_nav_rail_button,
            self.active_view
        ]
    
    @property
    def active_view(self):
        return self._active_view
    
    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()
        
    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.page.update()