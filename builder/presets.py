import tkinter as tk
from Globals import *

config_presets: dict = {
    "Reset": [],
    "Test": [
        {
            "type": "anntype",
            "value": "test"
        }
    ]
}


def add_to_panel(panel: tk.Frame, widget_type: str, value=None):
    parent = panel.parent
    if panel.active_col == 3:
        panel.active_col = 0
        panel.active_row += 2
    try:
        wg_data = widget_types[widget_type]
    except KeyError:
        print(f"widget of type {widget_type} not found.")
        return
    wg_label = tk.Label(panel, text=wg_data["label"])
    wg_label.grid(row=panel.active_row, column=panel.active_col)

    wg = None

    if wg_data["type"] == "dropdown":
        temp_str_var = tk.StringVar()
        if value is not None:
            temp_str_var.set(value)
        panel.parent.call_chain.append(temp_str_var)
        wg = tk.OptionMenu(panel, temp_str_var, *wg_data["options"])
        if "command" in wg_data:
            temp_str_var.trace("w", wg_data["command"])
    elif wg_data["type"] == "adder":
        temp_str_var = tk.StringVar()
        wg = tk.OptionMenu(panel, temp_str_var, *wg_data["options"], command=
        lambda _: adder_callback(temp_str_var.get(),panel,wg_label))
        panel.adder = wg
        # if "command" in wg_data:
        #     temp_str_var.trace("w", wg_data["command"])
    if wg is not None:
        wg.grid(row=panel.active_row + 1, column=panel.active_col)

    panel.active_col += 1


def make_adder(frame: tk.Frame):
    add_to_panel(frame, "adder")


def reset(frame: tk.Frame):
    for i in frame.winfo_children():
        i.destroy()

    frame.parent.call_chain = []
    frame.active_row = 1
    frame.active_col = 0

    make_adder(frame)


def preset_reset(frame: tk.Frame):
    reset(frame)
    make_adder(frame)
