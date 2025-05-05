import 'package:flet/flet.dart';
import 'package:flutter/material.dart';

class LayoutBuilderControl extends StatefulWidget {
  final Control control;

  const LayoutBuilderControl({
    super.key,
    required this.control,
  });

  @override
  State<LayoutBuilderControl> createState() => _LayoutBuilderControlState();
}

class _LayoutBuilderControlState extends State<LayoutBuilderControl>
    with FletStoreMixin {
  Size? _lastSize;
  bool _hasInitialized = false;
  bool _updateOnBuild = false;

  void sendEvent(String name, [dynamic data]) {
    widget.control.triggerEvent(name, data);
  }

  @override
  void initState() {
    super.initState();
    _updateOnBuild = widget.control.getBool("update_size_on_init") ?? false;
  }

  void onChange(double width, double height) {
    sendEvent("on_change", {
      "width": width,
      "height": height,
    });
    print("LayoutBuilder dimensions: Width: ${width}, Height: ${height}");
  }

  @override
  Widget build(BuildContext context) {
    print("Stack with layout builder build: ${widget.control.id}");

    var content = widget.control.buildWidget("content");

    Widget? child = content;

    var layout = LayoutBuilder(
      builder: (BuildContext context, BoxConstraints constraints) {
        WidgetsBinding.instance.addPostFrameCallback((_) {
          final Size currentSize =
              Size(constraints.maxWidth, constraints.maxHeight);

          onChange(constraints.maxWidth, constraints.maxHeight);

          _hasInitialized = true;
          _lastSize = currentSize;

          child = child;
        });
        return Container(
            clipBehavior: Clip.none,
            alignment: widget.control.getAlignment("alignment"),
            child: child);
      },
    );

    return ConstrainedControl(
      control: widget.control,
      child: layout,
    );
  }
}
