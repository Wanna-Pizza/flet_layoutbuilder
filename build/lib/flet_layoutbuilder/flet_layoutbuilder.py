from dataclasses import dataclass, field
from typing import Optional, Callable, Any

import flet as ft


__all__ = ["LayoutBuilder", "LayoutEvent"]


@dataclass
class LayoutEvent(ft.ControlEvent):
    height: Optional[float] = field(metadata={"data_field": "height"})
    width: Optional[float] = field(metadata={"data_field": "width"})

@ft.control("LayoutBuilder")
class LayoutBuilder(ft.ConstrainedControl, ft.AdaptiveControl):
    """
    A LayoutBuilder is a control that allows for dynamic layout changes based on the size of its parent.
    It triggers events when the layout dimensions change, enabling responsive design.
    """
    expand: Optional[bool | int] = False
    alignment: Optional[ft.Alignment] = None
    content: Optional[ft.Control] = None
    update_size_on_init: Optional[bool] = False
    on_change: ft.OptionalEventCallable["LayoutEvent"] = None