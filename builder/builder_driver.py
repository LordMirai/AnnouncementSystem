import os
import stringbuilder as sb
from graphics import GUI
from Globals import *


def sound_check(inexistent_only=False):
    all_sounds = {*announcement_types.values(), *target_types.values(), *orders.values(), *locations.values(),
                  *preset_messages.values(), *basic_number_dict.values(), *conjunctions.values(), *events.values(),
                  *flavor.values(), *letters, *numeric_modifiers}
    for i in numeric_modifiers:
        all_sounds.add(i.lower())
    all_sounds.remove("")
    sounds = sorted(list(all_sounds))

    print(f"\nSound test: {len(sounds)} to be checked.")
    missing = 0

    for i in sounds:
        path = f"../sounds/{i}.wav"
        if os.path.exists(path):
            if not inexistent_only:
                print(f"'{i}' exists!")
        else:
            print(f"'{i}' not found")
            missing += 1

    print(f"[{missing}] sound files are missing")


def drive_builder():
    sound_check(True)
    GUI()
    # sb.vox("order guard three five three pause repto lcz")
    pass


if __name__ == "__main__":
    drive_builder()
