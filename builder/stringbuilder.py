import simpleaudio as sa
from Globals import *


def vox(struct: str):
    struct = struct.replace(".", "pause").replace(",", "shortpause").replace("-", " ")
    print(f"Voicing structure '{struct}'")
    str_arr = struct.split(" ")

    for itm in str_arr:
        if itm == " " or itm == "":
            continue
        filename = "../sounds/" + itm + '.wav'
        try:
            obj = sa.WaveObject.from_wave_file(filename)
            play_obj = obj.play()
            play_obj.wait_done()
        except FileNotFoundError:
            print(f"[Vox] FnFe. No recorded line for '{itm}'.")


def build_number(number) -> str:
    thousands = ""
    hundreds = ""
    tens = ""
    digit = ""
    adlit = False

    if number.startswith("^"):
        adlit = True
        number = number[1:]
    if number == "-" or number == "":  # ignored
        return ""
    try:
        tmp = int(number)
    except ValueError:
        return "invnum"

    if tmp == 0:
        return "zero"
    if tmp >= 10000 or tmp < 0 or adlit:  # out of range
        return ad_literam_numbers(tmp)

    if tmp // 1000 > 0:
        dg = tmp // 1000
        thousands = f"{basic_number_dict[dg]}-thousand"
        tmp -= dg * 1000
    if tmp // 100 > 0:
        dg = tmp // 100
        hundreds = f"{basic_number_dict[dg]}-hundred"
        tmp -= dg * 100

    if tmp // 10 >= 2:
        dg = tmp // 10
        tens = basic_number_dict[dg * 10]
        tmp -= dg * 10
        if hundreds != "":
            tens = "and " + tens
    elif tmp // 10 == 1:
        tens = basic_number_dict[tmp]  # e.g. "twelve"
        tmp = 0

    if tmp > 0:
        digit = basic_number_dict[tmp]

    return " ".join([x for x in (thousands, hundreds, tens, digit) if x != ""]).strip()


def parse_full(inp) -> str:
    out_str = " ".join(inp)
    out_str = out_str.replace("--", " dash ")
    out_str = out_str.replace("-", " ")

    while "  " in out_str:
        out_str = out_str.replace("  ", " ")

    return out_str


def ad_literam_numbers(num_in: int) -> str:
    output = []
    if num_in < 0:
        output.append("minus")

    num = str(abs(num_in))
    while num != "":
        dict_val = basic_number_dict[int(num[0])]
        output.append(dict_val)
        num = num[1:]

    print("ad literam: ", " ".join(output))
    return " ".join(output)
