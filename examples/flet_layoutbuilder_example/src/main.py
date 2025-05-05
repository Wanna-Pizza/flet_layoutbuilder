import flet as ft

from flet_layoutbuilder import LayoutBuilder


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Text("Resize the window to see the LayoutBuilder in action"),
        LayoutBuilder(
            content=ft.Container(bgcolor='red',expand=True,content=ft.Text("Hello World"),alignment=ft.Alignment.center()),
            update_size_on_init=True,
            alignment=ft.Alignment.center(),
            expand=True,
            on_change=lambda e: print(e)
        ),
    )


ft.app(main)