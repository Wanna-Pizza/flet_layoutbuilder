# Introduction

FletLayoutbuilder for Flet.

## Examples

```
import flet as ft

from flet_layoutbuilder import FletLayoutbuilder


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletLayoutbuilder(
                    tooltip="My new FletLayoutbuilder Control tooltip",
                    value = "My new FletLayoutbuilder Flet Control", 
                ),),

    )


ft.app(main)
```

## Classes

[FletLayoutbuilder](FletLayoutbuilder.md)


