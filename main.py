import tkinter as tk
import csv
from PIL import Image, ImageTk
import charBuilder

HEADER_FONT = ("Optima", 24, "italic")
SMALL_FONT = ("Optima", 16)

d={}
with open('creaturelist.csv', encoding = "ISO-8859-1") as csvfile:
    table = csv.DictReader(csvfile)
    for row in table:
        creaturelist = {row['name']:[row['ac'],row['init']]}
        print(creaturelist)

class MainProg(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("DnD Battle Builder")

        self.frames = {}

        for F in (StartPage, CurrentBattle, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nwes")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="DnD Battle Builder", font=HEADER_FONT)
        label.grid(row=0, column=0, padx=500, pady=[200,50])

        newbattleButton = tk.Button(self, text="new battle", height="2", width="9", font=SMALL_FONT,
                                    command=lambda: controller.show_frame(CurrentBattle))
        newbattleButton.grid(row=1, column=0, pady=[0,10])

        loadbattleButton = tk.Button(self, text="load battle", height="2", width="9", font=SMALL_FONT)
        loadbattleButton.grid(row=3, column=0)


class CurrentBattle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Current Battle", font=HEADER_FONT)
        label.grid(row=0, column=4, pady=[10,10], padx=100)

        savebutton = tk.Button(self, text="save battle", font=SMALL_FONT)
        savebutton.grid(row=0,column=0,padx=10)
        loadbutton = tk.Button(self, text="load battle", font=SMALL_FONT)
        loadbutton.grid(row=0, column=1, padx=10)
        newbutton = tk.Button(self, text="new battle", font=SMALL_FONT)
        newbutton.grid(row=0, column=2, padx=10)


        homebutton = tk.Button(self, text="visit start page", font=SMALL_FONT,
                            command=lambda: controller.show_frame(StartPage))
        homebutton.grid(row=0, column=3, padx=10)

        newcharbutton = tk.Button(self, text="add player from library", font=SMALL_FONT)
        newcharbutton.place(x=400, y=120)

        newcharbutton = tk.Button(self, text="add new player", font=SMALL_FONT)
        newcharbutton.place(x=420, y=160)

        newmonbutton = tk.Button(self, text="add creature from library", font=SMALL_FONT)
        newmonbutton.place(x=580, y=120)

        newcharbutton = tk.Button(self, text="add new creature", font=SMALL_FONT,
                                  command=lambda: self.addchar(controller))
        newcharbutton.place(x=600, y=160)

    def addchar(self, controller):
        var = tk.StringVar()
        textbox = tk.Entry(controller, textvariable=var)
        textbox.focus_set()
        textbox.place(x=780, y=100)




class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", font=HEADER_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Start Page", font=SMALL_FONT,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit Current Battle", font=SMALL_FONT,
                            command=lambda: controller.show_frame(CurrentBattle))
        button2.pack()

app = MainProg()
app.geometry("1200x700")
app.mainloop()
