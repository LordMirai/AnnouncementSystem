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
    "D-": "d",
    "Agent": "agent",
    "Guard": "guard",
    "GenSec": "gensec",
    "Mobile Task Force": "mtf",
    "Engineer": "engineer",
    "Specialist": "specialist",
    "Tech Expert": "techie",
    "Medic": "medic",
    "Civilian": "civilian",
    "Intruder": "intruder",
    "MTF E-11 NTF": "ntf_full",  # "Mobile Task Force Epsilon-11, designated Nine Tailed Fox"
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

letters = {
    '',
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
}

orders = {
    "": "",
    "Present to": "presto",
    "Report at": "repat",
    "Report to": "repto",
    "Report position": "reppos",
    "Status Report": "strep",
    "Secure": "secure",
    "Secure and Hold": "sechold",
    "Contain": "contain",
    "Terminate": "terminate",
    "Take point": "takepoint",
    "Go to": "goto",
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
    "Retrieve": "retrieve"
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
    "Medical Bay": "medbay",
    "Science Lab": "scilab",
    "Inanimate Object Storage": "ios"

}

preset_messages = {
    "": "",
    "SCP Containment Breach": "contbreach",
    "Site Anomaly": "sian",
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

conjunctions = {
    "": "",
    "and": "and",
    "or": "or",
    "not": "not",
    "for": "for",
    "at": "at",
    "to": "to",
    "with": "with",
    "between": "between",
    "is": "is",
    "by": "by",
    "designated": "designated",
    "has": "has",

}

events = {
    "": "",
    "has been contained": "beencontained",
    "needed at": "needat",
    "requested at": "reqat",
    "detected": "detected",
    "has entered the facility": "hasentered",
    "has left the facility": "hasleft",
}

flavor = {
    "": "",
    "immediately": "immediately",
    "carefully": "carefully",
    "when done": "wdone",
    "if possible": "ifpos",
    "please": "please"
}

objects = {
    "": "",
    "Object": "obj",
    "Item": "item",
    "Weapon": "wpn",
    "Keycard": "card",
    "SCP Containment beam": "contbeam",
    "Vial, Beaker or Flask": "vial"
}


def adder_callback(val, panel, label):
    panel.adder.destroy()
    label.destroy()
    from builder import presets

    panel.active_col -= 1  # to counter the removal

    presets.add_to_panel(panel, adder_types[val])
    presets.make_adder(panel)


adder_types = {
    "Announcement Type": "anntype",
    "Message": "msg",
    "Order": 'order',
    "Text": 'text',
    "Number": 'num',
    "Letter": 'lett',
    "Entity": 'ent',
    "Period": '.',
    "Comma": ",",
    "Conjunction": "conj",
    "Modifier": "mod",
    "Location": "loc",
    "Event": "ev",
    "Flavor": "flav"
}

widget_types: dict = {
    "adder": {
        "type": "adder",
        "label": "Add new",
        "options": adder_types,
        "command": adder_callback
    },
    "anntype": {
        "type": "dropdown",
        "label": "Announcement Type",
        "options": announcement_types
    },
    "msg": {
        "type": "dropdown",
        "label": "Preset Message",
        "options": preset_messages
    },
    ".": {
        "type": "checkbox",
        "label": "'.'"
    },
    ",": {
        "type": "checkbox",
        "label": "','"
    },
    "text": {
        "type": "plaintext",
        "label": "Text"
    },
    "ent": {
        "type": "dropdown",
        "label": "Entity/Person",
        "options": target_types
    },
    "num": {
        "type": "plaintext",
        "label": "Number (^ = ad lit.)"
    },
    "order": {
        "type": "dropdown",
        "label": "Orders",
        "options": orders
    },
    "loc": {
        "type": "dropdown",
        "label": "Location",
        "options": locations
    },
    "mod": {
        "type": "dropdown",
        "label": "Modifier",
        "options": numeric_modifiers
    },
    "conj": {
        "type": "dropdown",
        "label": "Conjunction",
        "options": conjunctions
    },
    "ev": {
        "type": "dropdown",
        "label": "Event",
        "options": events
    },
    "flav": {
        "type": "dropdown",
        "label": "Flavor text",
        "options": flavor
    },
    "lett": {
        "type": "dropdown",
        "label": "Letter",
        "options": letters
    },
    "obj": {
        "type": "dropdown",
        "label": "Object",
        "options": objects
    },
}
