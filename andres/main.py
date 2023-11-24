import flet
import time

def main(page: flet.Page):
    page.title= "Light spectre controled with python"
    col = flet.Column(
        controls=[
            flet.Row(
                controls=[
                    flet.Text(value="Doing andres' homework"),
                    flet.Slider(),
                ],
            ),
            flet.Column(
                controls=[
                    flet.Image(
                        src="https://picsum.photos/200/200?random=1"
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

flet.app(target=main, view=flet.AppView.WEB_BROWSER)