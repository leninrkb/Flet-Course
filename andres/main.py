import flet
import time

def main(page: flet.Page):
    page.title= "Light spectre controled with python"
    col = flet.Column(
        controls=[
            flet.Row(
                controls=[
                    flet.Text(value="Doing andres homework"),
                    flet.Slider(
                        
                    ),
                ],
            ),
            flet.Column(
                controls=[
                    flet.Image(
                        src=f"/images/arabian_cat.png",
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