import time
from tkinter import *
from word_generate import generate
from create_cell import *
from tkinter import ttk
from PIL import ImageTk, Image
from itertools import count, cycle
class ImageLabel(Label):
    def load(self, im):
        im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        self.frames = cycle(frames)
        self.delay = im.info["duration"]

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.after(self.delay, self.next_frame)

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

def dwindow():
    window = Tk()
    window.geometry("500x500")
    window.title("5 БУКВ")
    window["bg"] = "gray22"
    window.resizable(False, False)
    answer = generate()
    print(answer)

    alphabet = {}
    num = 0
    st = 'ёйцукенгшщзхъфывапролджэячсмитьбю'
    for letter in st:
        num += 1
        letter_alphabetter = Label(
            window,
            text = letter,
            font='Arial 10 bold',
            bg="gray22",
            fg="white",
            highlightbackground="black",
            highlightthickness=1,
            height = 2,
            width = 4,
        )
        alphabet[letter] = letter_alphabetter
        if num <= 9:
            letter_alphabetter.place(relx=0.02, rely=0.05 + num * 0.09)
        elif num <= 18:
            letter_alphabetter.place(relx=0.11, rely=0.05 + (num - 9) * 0.09)
        elif num <= 26:
            letter_alphabetter.place(relx=0.20, rely=0.05 + (num - 17) * 0.09)
        elif num <= 33:
            letter_alphabetter.place(relx=0.29, rely=0.05 + (num - 24) * 0.09)

    title5 = Label(
        window,
        height=1,
        width=2,
        text="5",
        font=("Arial", 30, "bold"),
        fg="yellow",
        bg="black",

    )
    title5.place(relx=0, rely=0)

    title_b = Label(
        window,
        text="Б  У  К  В",
        font=("Arial", 30, "bold"),
        fg="#000000",
        bg="yellow",
        width=10,
        justify=LEFT
    )
    title_b.place(relx=0.11, rely=0)

    cell = {}
    x = y = 0
    for i in range(1, 31):
        cell[f"square{i}"] = create_cell(window)
        cell[f"square{i}"].place(relx=0.4 + 0.11 * x, rely=0.14 + 0.11 * y)
        x += 1
        if i % 5 == 0:
            y += 1
            x = 0
    cell[f"square1"].focus()

    def restart_func():
        window.destroy()
        dwindow()

    def restart():
         #image = ImageTk.PhotoImage(file='free-icon-repeat-11333414.png')
         restart_button = Button(window,
                                 text="Restart",
                                 font = "Tahoma 12 bold",
                                 fg = "yellow",
                                 #image = image,
                                 height = 2,
                                 width = 6,
                                 bg = "green",
                                 command=restart_func
                                 )
         restart_button.place(relx=0.8, rely=0.8)


    def win_gif():
        lb = ImageLabel(window)
        lb.pack(expand=1, fill="both")
        lb.load('seasam.gif')

        win_label = Label(window,
                          text="YOU WIN",
                          font=("Tahoma", 30, "bold"),
                          fg="white",
                          bg="green",
                          width=16,
                          justify="center",
                          anchor=N,
                          borderwidth=1,
                          relief="solid",
                          highlightthickness=7,
                          highlightbackground="yellow",
                          highlightcolor="yellow",
                          )
        win_label.place(relx=0.1, rely=0)

    def check_word(e):
        for row in range(1, 27, 5):
            count = 0
            if not cell[f"square{row}"].get() == "":
                for i in range(row, row + 5):
                    val = cell[f"square{i}"]
                    if not val.get() in answer:
                        alphabet[val.get()].config(bg="#1A1A1A", fg="white")
                    elif val.get() in answer:
                        val.config(bg="white", fg="black")
                        alphabet[val.get()].config(bg="white", fg="black")
                    if answer[(i - 1) % 5] == val.get():
                        val.config(bg="yellow", fg="black")
                        alphabet[val.get()].config(bg="yellow", fg="black")
                        count += 1
            if count == 5:
                win_gif()
                restart()
            if count != 5 and not cell[f"square30"].get() == "":
                lb = ImageLabel(window)
                lb.pack(expand=1, fill='x')
                lb.load('orig.gif')

                lose_label = Label(window,
                                  text="YOU LOSE",
                                  font=("Tahoma", 30, "bold"),
                                  fg="white",
                                  bg="red",
                                  width=16,
                                  justify="center",
                                  anchor=N,
                                  borderwidth=1,
                                  relief="solid",
                                  highlightthickness=7,
                                  highlightbackground="yellow",
                                  highlightcolor="yellow",
                                  )
                lose_label.place(relx=0.1, rely=0)
                ans_lab = Label(window,
                                text=answer,
                                font=("Tahoma 20 bold"),
                                fg="white",
                                bg = "red",
                                justify="center",
                                width=30,
                                anchor = CENTER
                                )
                ans_lab.place(relx=0, rely=0.51)

                restart()


    check = Button(
        window,
        bg="yellow",
        text="ОК",
        font=("Arial", 15, "bold"),
        #command=check_word
    )
    check.bind("<Button-1>", check_word)
    check.place(relx=0.85, rely=0.85)

    ######################################################
    window.mainloop()