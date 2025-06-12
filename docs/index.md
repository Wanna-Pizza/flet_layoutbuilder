# Flet LayoutBuilder

**Flet LayoutBuilder** is a tool for building adaptive, responsive interfaces in Python using the Flet library.

---

## Usage Example

Here is a basic example of using LayoutBuilder in a Flet Python application:

```python
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
            content=ft.Container(
                bgcolor='red',
                expand=True,
                content=ft.Text("Hello World"),
                alignment=ft.Alignment.center()
            ),
            expand=True,
            on_change=on_change,
            update_size_on_init=True  # <--- new parameter explained below
        ),
    )

ft.app(main)
```

---

## How It Works

- **LayoutBuilder** is a special widget that lets you react to changes in the size of its parent container. It calls your `on_change` callback with updated dimensions whenever the size changes.
- **content** is the main widget placed inside the LayoutBuilder. In this example, it's a red `Container` with centered text.
- **expand=True** makes both the LayoutBuilder and its content occupy all available space.
- **on_change** is a callback function called whenever the LayoutBuilder size changes. In the example, it updates the text on the page with the current width and height.
- **update_size_on_init** (bool):  
  If set to `True`, the `on_change` callback will be called immediately on widget initialization, passing the current size to your handler.  
  This means your function gets the actual size right away, not only after the first resize event.  
  Default is `False`.

### Important!

> **LayoutBuilder works only with widgets that support the `expand` parameter.**  
> When specifying `content`, you must use widgets that have the `expand` property (such as `Container`, `Row`, `Column`, etc., with `expand=True`).  
> This is required for LayoutBuilder to properly manage their size and provide responsive behavior.

---

## Use Cases

- **Responsiveness:** Build interfaces that adapt to the screen size.
- **Interactivity:** Dynamically change content or behavior when the widget is resized.
- **Immediate size awareness:** With `update_size_on_init=True`, your handler gets the actual size even before any manual resizing.
- **Convenience:** No need to manually track sizes—LayoutBuilder automatically calls your handler when needed.

---

## LayoutBuilder API (Python)

```python
LayoutBuilder(
    content: ft.Control,           # Widget that MUST support 'expand'
    expand: bool = False,          # Occupy all available space if True
    on_change: Callable = None,    # Callback receiving new sizes
    update_size_on_init: bool = False, # If True, call on_change at init with current size
    # other parameters...
)
```

- `content` — The main widget inside LayoutBuilder. MUST support the `expand` parameter.
- `expand` — If True, LayoutBuilder takes all available space.
- `on_change(e)` — Callback called with an object containing `width` and `height` whenever the size changes.
- `update_size_on_init` — If True, calls `on_change` immediately after widget is created, passing the initial size.

---

## Examples

- Build adaptive panels that rearrange depending on width.
- Implement different layouts for mobile and desktop screens.
- Dynamically show or hide UI elements based on available space.

---

## Documentation

- See the `/examples` folder for more usage examples.
- Up-to-date docs and examples are available on GitHub Pages:  
  https://wanna-pizza.github.io/flet_layoutbuilder/

---

**Flet LayoutBuilder** — the simple way to add adaptivity to your Python Flet apps!
