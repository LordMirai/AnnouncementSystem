import tkinter as tk
import stringbuilder as sb
from Globals import *


class GUI:
    # TODO: replace input1/2/3... with suggestive names. Do the same with outputs were needed
    def __init__(self):
        root = tk.Tk()
        root.title("Builder GUI")
        # root.geometry("600x600")
        root.bind("<Escape>", lambda _: root.destroy())

        self.announce_type = tk.StringVar(root)
        self.subj_type = tk.StringVar(root)
        self.subj_num = tk.StringVar(root)
        self.subj_num_modif = tk.StringVar(root)
        self.tg_num_modif = tk.StringVar(root)
        self.order = tk.StringVar(root)
        self.tg_type = tk.StringVar(root)
        self.location = tk.StringVar(root)
        self.preset_msg = tk.StringVar(root)
        self.tg_num = tk.StringVar(root)
        self.say_at = tk.BooleanVar(root)
        self.include_period = tk.BooleanVar(root)

        # var setters
        self.announce_type.set("General Announcement")
        self.say_at.set(False)
        self.include_period.set(False)

        self.root = root
        self.populate_options()

        self.populate_presets()

        root.mainloop()

    def populate_options(self):
        root = self.root
        # labels and options
        ann_type_lb = tk.Label(root, text="Announcement Type")
        ann_type_lb.grid(row=2, column=0)

        ann_type = tk.OptionMenu(root, self.announce_type, *announcement_types)
        ann_type.grid(row=3, column=0)

        pres_msg_lb = tk.Label(root, text="Preset Messages")
        pres_msg_lb.grid(row=2, column=1)

        pres_msg = tk.OptionMenu(root, self.preset_msg, *preset_messages)
        pres_msg.grid(row=3, column=1)

        inc_at = tk.Checkbutton(root, text='" . "', variable=self.include_period)
        inc_at.grid(row=3, column=2)

        subj_type_lb = tk.Label(root, text="Subject Type")
        subj_type_lb.grid(row=4, column=0)

        subj_type = tk.OptionMenu(root, self.subj_type, *target_types)
        subj_type.grid(row=5, column=0)

        num_lb = tk.Label(root, text="Number ('^' = ad literam)")
        num_lb.grid(row=4, column=2)

        num_in = tk.Entry(root, textvariable=self.subj_num)
        num_in.grid(row=5, column=2)

        num_modif_lb = tk.Label(root, text="Modifier")
        num_modif_lb.grid(row=4, column=1)

        num_modif = tk.OptionMenu(root, self.subj_num_modif, *numeric_modifiers)
        num_modif.grid(row=5, column=1)

        order_lb = tk.Label(root, text="Order")
        order_lb.grid(row=6, column=0)

        order = tk.OptionMenu(root, self.order, *orders)
        order.grid(row=7, column=0)

        tg_type_lb = tk.Label(root, text="Target Type")
        tg_type_lb.grid(row=8, column=0)

        tg_type = tk.OptionMenu(root, self.tg_type, *target_types)
        tg_type.grid(row=9, column=0)

        num_modif_lb = tk.Label(root, text="Target Modifier")
        num_modif_lb.grid(row=8, column=1)

        tg_num_modif = tk.OptionMenu(root, self.tg_num_modif, *numeric_modifiers)
        tg_num_modif.grid(row=9, column=1)

        tg_num_lb = tk.Label(root, text="Target Number")
        tg_num_lb.grid(row=8, column=2)

        tg_num_in = tk.Entry(root, textvariable=self.tg_num)
        tg_num_in.grid(row=9, column=2)

        inc_at = tk.Checkbutton(root, text='Include "at"?', variable=self.say_at)
        inc_at.grid(row=11, column=0)

        loc_lb = tk.Label(root, text="Location")
        loc_lb.grid(row=10, column=1)

        location = tk.OptionMenu(root, self.location, *locations)
        location.grid(row=11, column=1)

        vox_button = tk.Button(root, text="Vox", command=self.vox_cb)
        vox_button.grid(row=12, column=0, columnspan=10, ipadx=20, pady=5)

    def vox_cb(self):
        strings = [
            str(self.announce_type.get()),
            str(self.subj_type.get()),
            str(self.subj_num.get()),
            str(self.subj_num_modif.get()),
            str(self.tg_num_modif.get()),
            str(self.order.get()),
            str(self.tg_type.get()),
            str(self.location.get()),
            str(self.preset_msg.get()),
            str(self.tg_num.get()),
            '1' if self.say_at.get() else '0',
            '1' if self.include_period.get() else '0'
        ]

        pretty = f"{self.announce_type.get()}: {self.preset_msg.get()}{'.' if self.include_period.get() else ''} " \
                 f"{self.subj_type.get()} " \
                 f"{self.subj_num_modif.get() + '-' if self.subj_num_modif.get() != '' else ''}" \
                 f"{self.subj_num.get().replace('-', '') if self.subj_num.get() == '-' else self.subj_num.get()} " \
                 f"{self.order.get()} {self.tg_type.get()} " \
                 f"{self.tg_num_modif.get() + '-' if self.tg_num_modif.get() != '' else ''}" \
                 f"{self.tg_num.get()} {'at' if self.say_at.get() else ''} {self.location.get()}"

        while "  " in pretty:
            pretty = pretty.replace("\n", " ")
            pretty = pretty.replace("  ", " ")

        print(f"Pretty output: {pretty}")

        parsed = sb.parse_full(strings)
        print(f"parsed: {parsed}")
        # sb.vox(parsed)

    def load_preset(self, preset):
        self.announce_type.set(preset["annt"])
        self.preset_msg.set(preset["pm"])
        self.include_period.set(preset["per"])
        self.subj_type.set(preset["st"])
        self.subj_num_modif.set(preset["sumod"])
        self.subj_num.set(preset["num"])
        self.order.set(preset['order'])
        self.tg_type.set(preset['tt'])
        self.tg_num_modif.set(preset['tmod'])
        self.tg_num.set(preset['tnum'])
        self.say_at.set(preset['at'])
        self.location.set(preset['loc'])

    def populate_presets(self):
        rowstart = 14

        for k, v in config_presets.items():
            tk.Button(self.root, text=k, command=lambda: self.load_preset(v)).grid(row=rowstart, column=0)
            rowstart += 1