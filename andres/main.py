import flet
import time

def main(page: flet.Page):
    page.title= "Light spectre controled with python"
    file = flet.Text()
    def filepicked(e:flet.FilePickerResultEvent):
        if e.files:
            r = list(map(lambda f: f.name, e.files))
            file.value = r[0]
            file.update()
    file_picker_dialog = flet.FilePicker(on_result=filepicked)
    page.overlay.append(file_picker_dialog)
    col = flet.Column(
        controls=[
            flet.Row(
                spacing= 5,
                controls=[
                    flet.Column(
                        spacing= 5,
                        controls=[
                            file,
                            flet.OutlinedButton(
                                icon= flet.icons.FILE_UPLOAD,
                                text= "Upload image",
                                on_click= lambda _: file_picker_dialog.pick_files()
                            ),
                        ]
                    ),
                    flet.Column(
                        controls=[
                            flet.Text(value="Hayase <3")
                        ]
                    )
                ],
            ),
            flet.Column(
                controls=[
                    file,
                    flet.Image(
                        src=f"/images/AOT.png",
                        width=100,
                        height=100,
                        fit=flet.ImageFit.CONTAIN,
                    )
                ]
            ),
            flet.Row(
                controls=[
                    flet.OutlinedButton(text="fit image")
                ]
            )
        ]
    )
    page.add(col)
    page.update()

flet.app(
    target=main,
    assets_dir="assets"
)