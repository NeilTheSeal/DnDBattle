import tkinter as tk
import csv
import time

HEADER_FONT = ("Optima", 24, "italic")
SMALL_FONT = ("Optima", 16)

creaturelist={}
creaturetable=[]

with open('creaturelist.csv', encoding = "ISO-8859-1") as csvfile:
    table = csv.DictReader(csvfile)
    for row in table:
        creaturelist = {row['name']:[row['ac'],row['init']]}
        creaturetable.append(row['name'])


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

        addcharbutton = tk.Button(self, text="add player from library", font=SMALL_FONT)
        addcharbutton.place(x=400, y=120)

        newcharbutton = tk.Button(self, text="add new player", font=SMALL_FONT)
        newcharbutton.place(x=420, y=160)

        addmonbutton = tk.Button(self, text="add creature from library", font=SMALL_FONT,
                                 command=lambda: [self.addmonster(controller)])
                                                  #monsterlist.activate(index=3),
                                                  #monsterlist.see(index=3)])
                                                  #helpful command: curselection()
        addmonbutton.place(x=580, y=120)

        newmonbutton = tk.Button(self, text="add new creature", font=SMALL_FONT,
                                  command=lambda: None)
        newmonbutton.place(x=600, y=160)

    def addmonster(self, controller):
        var = tk.StringVar()
        var.set("Aarakocra")
        textbox = tk.Entry(controller, textvariable=var, exportselection=True)
        textbox.focus_set()
        textbox.place(x=820, y=20)
        monsterlist = tk.Listbox(self, selectmode="single", height=10, width=30)
        for i in range(len(creaturetable)):
            monsterlist.insert(i, creaturetable[i])
        monsterlist.place(x=780, y=50)
        #monsterlist.activate(index=)
        #monsterlist.see(index=int(textbox.get()))
        addbutton = tk.Button(self, text="add", font=SMALL_FONT,
                                 command=lambda: self.updater())
        addbutton.place(x=800, y=260)
        return var.get()

    def updater(self):
        print(self.addmonster(self))
        self.after(20000,self.updater())


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
