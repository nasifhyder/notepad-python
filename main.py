from tkinter import *
from tkinter import ttk
from functions import save, bold, select, open_, normal
from functools import partial

option = ["Arial", "Algerian", "Courier"]
txt = "hello"


windows = Tk()
windows.title = "Text Editor"
windows.geometry("650x500")

text_area = Text(height=100, width=60)
text_area.grid(row=1, column=0, columnspan=4)
open_(text_area)

save_button = Button(text="Save", height=1, width=5, command=partial(save, text_area))
save_button.grid(row=0, column=0, sticky="w")

font_label = Label(text="Fonts: ", height=1, width=5)
font_label.grid(row=0, column=2, sticky="w")

font_option = ttk.Combobox(width=10, height=1)
font_option["values"] = option
font_option.grid(row=0, column=2, sticky="e")

select_button = Button(text="select", height=1, width=5, command=partial(select, font_option, text_area))
select_button.grid(row=0, column=3, sticky="w")

bold_button = Button(text="Bold", height=1, width=5, command=partial(bold, font_option, text_area))
bold_button.grid(row=0, column=1, sticky="w")

normal_button = Button(text="normal", height=1, width=5, command=partial(normal, font_option, text_area))
normal_button.grid(row=0, column=1, sticky="e")

windows.mainloop()
