import flet
import time
import os 
import cv2
import matplotlib.pyplot as plt


def newchart():
    return flet.LineChart(
        data_series=[],
        border= flet.border.all(3, flet.colors.with_opacity(0.2, flet.colors.ON_SURFACE)),
        horizontal_grid_lines= flet.ChartGridLines(
            interval= 1, 
            color= flet.colors.with_opacity(0.2, flet.colors.ON_SURFACE), 
            width= 1
        ),
        vertical_grid_lines= flet.ChartGridLines(
            interval=1, 
            color=flet.colors.with_opacity(0.2, flet.colors.ON_SURFACE), 
            width=1
        ),
        left_axis=flet.ChartAxis(
            labels=[
                flet.ChartAxisLabel(
                    value=1,
                    label=flet.Text("1"),
                ),
                flet.ChartAxisLabel(
                    value=10,
                    label=flet.Text("255"),
                ),
            ],
            labels_size=50,
        ),
        bottom_axis=flet.ChartAxis(
            labels=[
                flet.ChartAxisLabel(
                    value=1,
                    label=flet.Text("1")
                ),
                flet.ChartAxisLabel(
                    value=10,
                    label=flet.Text("255")
                ),
            ],
            labels_size=50,
        ),
        min_y=0,
        max_y=10,
        min_x=0,
        max_x=10,
        expand=True,        
    )

def make_linechart(chanel, color):
    line_chart_data = flet.LineChartData(
        stroke_width=2,
        color=color,
        curved=True,
        stroke_cap_round=True,
    )
    histogram = cv2.calcHist([chanel], [0], None, [10], [0, 256])
    max_ = max(histogram, key=lambda x: x[0])
    histogram = histogram / max_
    histogram = histogram * 10
    for i, j in enumerate(histogram):
        data_point = flet.LineChartDataPoint(i,j[0])
        line_chart_data.data_points.append(data_point)
    return line_chart_data
    

def main(page: flet.Page):
    page.title= "Light spectre controled with python"
    uploaded_files = os.listdir("./assets/uploads")
    chartB = newchart()
    chartG = newchart()
    chartR = newchart()
    
    images = flet.Row(
        expand= False,
        wrap= False,
        scroll= "always",
    )
    current_img = flet.Image(
        src=f"/images/arabian_cat.png",
        width=500,
        height=500,
        fit=flet.ImageFit.CONTAIN,
        border_radius= flet.border_radius.all(10),
    )
    def set_current_file(name):
        current_file.value = name
        current_file.update()
    def load_charts(e):
        src = f"./assets/uploads/{current_file.value}"
        data = cv2.imread(src)
        B, G, R = cv2.split(data)
        line_chart_b = make_linechart(B, flet.colors.BLUE)
        line_chart_g = make_linechart(G, flet.colors.GREEN)
        line_chart_r = make_linechart(R, flet.colors.RED)
        chartB.data_series = [line_chart_b]
        chartG.data_series = [line_chart_g]
        chartR.data_series = [line_chart_r]
        current_img.src = f"/uploads/{current_file.value}"
        current_img.update()
        chartB.update()
        chartG.update()
        chartR.update()
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
                    content= flet.Text(
                        value= name,
                        text_align= flet.TextAlign.CENTER,
                        width= 100,
                        max_lines= 1,
                        overflow= flet.TextOverflow.ELLIPSIS
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
        scroll= flet.ScrollMode.AUTO,
        spacing= 20,
        expand= True,
        controls=[
            flet.Row(
                scroll= flet.ScrollMode.AUTO,
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
                                            on_click= load_charts
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
            flet.Row(
                scroll= flet.ScrollMode.AUTO,
                controls=[
                    flet.Container(
                        content= chartB,
                        width= 400,
                        height= 450,
                    ),
                    flet.Container(
                        content= chartG,
                        width= 400,
                        height= 450,
                    ),
                    flet.Container(
                        content= chartR,
                        width= 400,
                        height= 450,
                    ),
                ],
            ),
            flet.Row(
                alignment= flet.MainAxisAlignment.CENTER,
                controls=[
                    flet.Container(
                        content= current_img,
                        padding= 5,
                        ink= True,
                        border_radius= 10,
                        border= flet.border.all(1, flet.colors.DEEP_PURPLE_500),
                    ),
                ],
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