
def save(txt_area):
    text = txt_area.get("1.0", "end")
    with open("text_editor.txt", "w") as txt:
        txt.write(text)


def bold(font_option, txt_area):
    font = font_option.get()
    txt_area.config(font=(font, 14, "bold"))


def normal(font_option, txt_area):
    font = font_option.get()
    txt_area.config(font=(font, 14, "normal"))


def font_changer(f, txt_area):
    txt_area.config(font=f)


def open_(txt_area):
    txt_area.delete("1.0", "end")
    with open("text_editor.txt", "r") as txt:
        text = txt.read()
        txt_area.insert("end", text)


def select(fnt_option, txt_area):
    fnt = fnt_option.get()
    font_changer(fnt, txt_area)

