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
    current_img = flet.Image(
        src=f"/images/arabian_cat.png",
        width=100,
        height=100,
        fit=flet.ImageFit.COVER,
        border_radius= flet.border_radius.all(10)
    )
    def set_current_file(name):
        current_file.value = name
        current_file.update()
    def set_current_img(e):
        current_img.src = f"/uploads/{current_file.value}"
        current_img.update()
        page.update()
    def add_img_images(src, name=""):
        _col = flet.Column(
            controls= [
                flet.Container(
                    content = flet.Image(
                        src= src,
                        width= 100,
                        height= 100,
                        border_radius= flet.border_radius.all(10),
                        fit= flet.ImageFit.COVER,
                    ),
                    on_click= lambda _: set_current_file(name),
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
                                text= "Select to upload",
                                on_click= lambda _: file_picker.pick_files()
                            ),
                            flet.OutlinedButton(
                                icon= flet.icons.UPLOAD_FILE,
                                text= "Upload",
                                on_click= upload
                            ),
                        ]
                    ),
                    flet.Container(
                        content= flet.Column(
                            controls=[
                                flet.Text("To upload:"),
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
                            horizontal_alignment= flet.CrossAxisAlignment.CENTER,
                            controls=[
                                flet.Container(
                                    content= flet.Text(
                                        value = "Current image:",
                                    ),   
                                ),
                                flet.Row(
                                    controls=[
                                        current_file,
                                        flet.TextButton(
                                            text= "Load charts",
                                            icon= flet.icons.INSERT_CHART,
                                            on_click= set_current_img
                                        )
                                    ]
                                ),
                                
                            ],
                        ),
                        padding= 5,
                        ink= True,
                        border_radius= 10,
                        border= flet.border.all(1, flet.colors.GREEN_500),
                    ),
                ],
            ),
            images,
            flet.Column(
                controls=[
                    flet.Container(
                        content= current_img,
                        padding= 5,
                        ink= True,
                        border_radius= 10,
                        border= flet.border.all(1, flet.colors.DEEP_PURPLE_500)
                    ),
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