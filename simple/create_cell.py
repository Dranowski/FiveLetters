import re
from tkinter import *
def create_cell(window):
    def is_valid(newval):
        return re.match("^[а-ё]?$", newval) is not None
    check = (window.register(is_valid), "%P")
    cell = Entry(window,
        bg="gray22",
        font=("Arial", 30, "bold"),
        fg="white",
        justify="center",
        width=2,
        borderwidth=1,
        relief="solid",
        highlightthickness=1,
        highlightbackground="yellow",
        highlightcolor="yellow",
        cursor="arrow",
        validate='key',
        validatecommand=check
    )

    def foo(e):
        if e.keycode != 9 and e.keycode != 13:
            cell.delete('0', END)
    cell.bind('<KeyPress>', foo)

    return cell