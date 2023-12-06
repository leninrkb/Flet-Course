import flet 

class Upload:
    def __init__(self, page:flet.Page):
        self.file_picker = flet.FilePicker(on_result=self.catch_file)
        page.overlay.append(self.file_picker)
        self.selected_file = None
        self.select_button = flet.FilledButton("Select file")
        
    def catch_file(self, e:flet.FilePickerResultEvent):
        if e.files:
            result = list(map(lambda f:f.name, e.files))
            self.selected_file = result[0]
            print(self.selected_file)
            
    def build(self):
        self.select_button.on_click = self.file_picker.pick_files
        return flet.Row(
            controls=[
                self.select_button
            ]
        )

def main(page:flet.Page):
    col = flet.Column(
        controls=[Upload(page)]
    )
    page.add(col)
    page.update()


flet.app(target=main)