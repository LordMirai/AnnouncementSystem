basic_number_dict = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

announcement_types = {
    '': '',
    "General Announcement": "genann",
    "Reminder": "reminder",
    "Alert": "alert",
    "Notice": "notice",
    "Site Anomaly": "sian",
    "Order": "order",
    "Imperative Order": "imporder",
    "Attention": "attention",
    "Emergency": "emergency",
    "Urgent": "urgent",
    "Important": "important",
    "Information": "info",
    "News": "news",
    "Event": "event",
    "Advice": "advice",
}

target_types = {
    "": "",
    "SCP": "scp",
    "Unit": "unit",
    "Researcher": "rsch",
    "D-Class": "dclass",
    "Agent": "agent",
    "Guard": "guard",
    "Scientist": "scientist",
    "Engineer": "engineer",
    "Specialist": "specialist",
    "Medic": "medic",
    "Civilian": "civilian",
    "Intruder": "intruder",
}

numeric_modifiers = [
    "",
    "Special",
    "Alpha",
    "Beta",
    "Gamma",
    "Delta",
    "Epsilon",
    "Zeta",
    "Theta",
    "Lambda",
    "Nu",
    "Omicron",
    "Sigma",
    "Omega",
]

orders = {
    "": "",
    "Present to": "presto",
    "Report at": "repat",
    "Report to": "repto",
    "Status Report": "strep",
    "Secure": "secure",
    "Secure and Hold": "sechold",
    "Contain": "contain",
    "Terminate": "terminate",
    "Take point": "takepoint",
    "Disperse": "disperse",
    "Disperse and Hold": "dishold",
    "Shakedown": "shakedown",
    "Patrol": "patrol",
    "Engage": "engage",
    "Designated for termination": "dfterm",
    "Arrest on sight": "aos",
    "Kill on sight": "kos",
    "Provide medical aid": "medaid",
    "Escort": "escort",
    "Escort to": "escortto",
    "Escort to and hold": "escorttohold",
}

locations = {
    '': '',
    "D-Block": "dblock",
    "Light Containment Zone": "lcz",
    "Heavy Containment Zone": "hcz",
    "Entrance Zone": "entrz",
    "Surface": "surface",
    "Pocket Dimension": "pocketdim",
    "Security": "security",
    "Light Containment Zone Checkpoint": "lczcp",
    "Heavy Containment Zone Checkpoint": "hczcp",
    "Entrance Zone Checkpoint": "entrzcp",
    "Personnel Wing": "pwing",
    "Non-Specialized SCPs": "nonspecscp",

}

preset_messages = {
    "": "",
    "SCP Containment Breach": "contbreach",
    "Unit Down": "undown",
    "MTF has arrived": "mtfarrived",
    "MTF has left": "mtfleft",
    "NTF has arrived": "ntfarrived",
    "NTF has left": "ntfleft",
    "Maintenance needed": "maintneeded",
    "Maintenance complete": "maintcomp",
    "SCP has been contained": "scpcontained",
    "SCP has been terminated": "scpterm",
    "Riot in progress": "riot",
    "Riot has ended": "riotend",
    "Keep doors closed": "rem_closedoors",
    "Report broken doors or objects": "rem_brokendoors",
    "We are here for you": "rem_wearehere",
}


def adder_callback(val, panel, label):
    print("adder called back")
    print(val, panel)
    panel.adder.destroy()
    label.destroy()
    from builder import presets
    presets.add_to_panel(panel, adder_types[val])
    presets.make_adder(panel)


adder_types = {
    "Announcement Type": "anntype",
    "Message": "msg",
    "Order": 'order',
    "Number": 'num',
    "Person": 'person',
    "Period": '.',
    "Comma": ",",
    "Conjunction": "conj",
    "Modifier": "mod",
    "Location": "loc"
}

widget_types: dict = {
    "anntype": {
        "type": "dropdown",
        "label": "Announcement Type",
        "options": announcement_types
    },
    "adder": {
        "type": "adder",
        "label": "Add new",
        "options": adder_types,
        "command": adder_callback
    }
}
