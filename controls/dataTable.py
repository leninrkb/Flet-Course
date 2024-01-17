import flet as ft
from flet import Page, Row, Column, Card, Container
from flet import TextButton, Text, TextField
from flet import DataTable, DataColumn, DataRow, DataCell


def main(page: Page):
    page.add(
        Card(
            expand=True,
            margin=10,
            content=DataTable(
                columns=[
                    DataColumn(Text("Name")),
                    DataColumn(Text("Surname")),
                    DataColumn(Text("Description")),
                ],
                rows=[
                    DataRow(
                        cells=[
                            DataCell(Text("Sana")),
                            DataCell(Text("Sunomiya")),
                            DataCell(Text("She's the love of my life")),
                        ]
                    )
                ],
            ),
        )
    )


ft.app(target=main)
