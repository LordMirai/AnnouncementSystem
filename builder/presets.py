import tkinter as tk
from Globals import *

config_presets = {
    "Reset": {
        "annt": "General Announcement",
        "pm": "",
        "per": False,
        "st": "",
        "sumod": "",
        "num": "",
        "order": "",
        "tt": "",
        "tmod": "",
        "tnum": "",
        "at": False,
        "loc": ""
    },
}


def add_to_panel(panel: tk.Frame, widget_type: str, label=""):
    if panel.active_col == 3:
        panel.active_col = 0
        panel.active_row += 2


def make_adder(frame: tk.Frame):
    add_to_panel(frame, "Add new widget", "adder")


def reset(frame: tk.Frame):
    for i in frame.winfo_children():
        i.destroy()
    make_adder(frame)


def preset_reset(frame: tk.Frame):
    reset(frame)
    make_adder(frame)


def update_parent(frame: tk.Frame):
    parent = frame.master


