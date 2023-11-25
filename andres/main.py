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
    file_picker = flet.FilePicker(on_result=filepicked)
    page.overlay.append(file_picker)
    def upload(e):
        to_upload = []
        if file_picker.result != None and file_picker.result.files != None:
            _file = file_picker.result.files[0]
            to_upload.append(
                flet.FilePickerUploadFile(
                    _file.name,
                    page.get_upload_url(_file.name, 600)
                )
            )
            file_picker.upload(to_upload)
            print(f"uploaded {_file.name}")
    col = flet.Column(
        controls=[
            flet.Row(
                controls=[
                    flet.Column(
                        controls=[
                            file,
                            flet.OutlinedButton(
                                icon= flet.icons.FOLDER,
                                text= "Select image",
                                on_click= lambda _: file_picker.pick_files()
                            ),
                            flet.OutlinedButton(
                                icon= flet.icons.FOLDER,
                                text= "Uplaod image",
                                on_click= upload
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
    assets_dir="assets",
    upload_dir="uploads"
)