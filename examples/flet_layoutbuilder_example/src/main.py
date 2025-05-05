import flet as ft

from flet_layoutbuilder import LayoutBuilder


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    text = ft.Text("Resize the window to see the LayoutBuilder in action")
    def on_change(e):
        text.value = f"Width: {e.width}, Height: {e.height}"
        text.update()
    page.add(
        text,
        LayoutBuilder(
            content=ft.Container(bgcolor='red',expand=True,content=ft.Text("Hello World"),alignment=ft.Alignment.center()),
            expand=True,
            on_change=on_change
        ),
    )


ft.app(main)