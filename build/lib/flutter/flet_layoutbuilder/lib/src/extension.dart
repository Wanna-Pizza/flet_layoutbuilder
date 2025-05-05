import 'package:flet/flet.dart';
import 'package:flutter/cupertino.dart';

import 'flet_layoutbuilder.dart';

class Extension extends FletExtension {
  @override
  Widget? createWidget(Key? key, Control control) {
    switch (control.type) {
      case "LayoutBuilder":
        return LayoutBuilderControl(
          control: control,
        );
      default:
        return null;
    }
  }
}
