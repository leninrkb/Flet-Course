import flet
import time
import os 


def main(page: flet.Page):
    page.title= "Light spectre controled with python"
    uploaded_files = os.listdir("./assets/uploads")
    images = flet.Row(
        expand= False,
        wrap= False,
        scroll= "always",
    )
    def add_img_images(src, name=""):
        _col = flet.Column(
            controls= [
                flet.Container(
                    content = flet.Image(
                        src= src,
                        width= 100,
                        height= 100,
                        border_radius= flet.border_radius.all(10),
                        fit= flet.ImageFit.COVER
                    ),
                ),
                flet.Container(
                    width= 100,
                    content= flet.Text(
                        value= name,
                        text_align= flet.TextAlign.CENTER
                    )
                )
            ],
        )
        images.controls.append(_col)
    for name in uploaded_files:
        add_img_images(f"/uploads/{name}", name)
    file = flet.Text(
        value= "",
        size= 14,
        color= flet.colors.BLUE_300,
        italic= True
    )
    current_file = flet.Text(
        value= "",
        size= 14,
        color= flet.colors.BLUE_300,
        weight= flet.FontWeight.BOLD
    )
    def filepicked(e:flet.FilePickerResultEvent):
        if e.files:
            r = list(map(lambda f: f.name, e.files))
            file.value = r[0]
            file.update()
    file_picker = flet.FilePicker(on_result=filepicked)
    page.overlay.append(file_picker)
    def notify(message):
        page.snack_bar = flet.SnackBar(
            content= flet.Text(
                value=message
            )
        )
        page.snack_bar.open = True
        page.update()
    def upload_file():
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
    def upload(e):
        if file.value != "":
            upload_file()
            time.sleep(1)
            add_img_images(f"/uploads/{file.value}", file.value)
            file.value = ""
            file.update()
            notify(f"{file.value} uploaded!")
        else:
            notify("Please select an image!")
            
    col = flet.Column(
        controls=[
            flet.Row(
                controls=[
                    flet.Column(
                        controls=[
                            flet.OutlinedButton(
                                icon= flet.icons.FOLDER,
                                text= "Select image",
                                on_click= lambda _: file_picker.pick_files()
                            ),
                            flet.OutlinedButton(
                                icon= flet.icons.UPLOAD_FILE,
                                text= "Upload image",
                                on_click= upload
                            ),
                        ]
                    ),
                    flet.Container(
                        content= flet.Column(
                            controls=[
                                flet.Text("Selected image:"),
                                file,
                            ],
                        ),
                        padding= 5,
                        ink= True,
                        border_radius= 10,
                        border= flet.border.all(1, flet.colors.DEEP_PURPLE_500)
                    ),
                    flet.Container(
                        content= flet.Column(
                            controls=[
                                flet.Text("Current image:"),
                                current_file,
                            ],
                        ),
                        padding= 5,
                        ink= True,
                        border_radius= 10,
                        border= flet.border.all(1, flet.colors.GREEN_500)
                    ),
                ],
            ),
            images,
            flet.Column(
                controls=[
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
    view= flet.WEB_BROWSER,
    assets_dir="assets",
    upload_dir="assets/uploads"
)