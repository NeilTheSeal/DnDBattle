from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):

        self.master.title("BATTLE!")

        self.pack(fill=BOTH, expand=1)

        newbattleButton = Button(self, text="new battle", height="2", width="9")
        newbattleButton.place(x=10, y=0)

        savebattleButton = Button(self, text="save battle", height="2", width="9")
        savebattleButton.place(x=110, y=0)

        loadbattleButton = Button(self, text="load battle", height="2", width="9")
        loadbattleButton.place(x=210, y=0)

        addallyButton = Button(self, text="add ally", height="2", width="9")
        addallyButton.place(x=310, y=0)

        addenemyButton = Button(self, text="add enemy", height="2", width="9")
        addenemyButton.place(x=410, y=0)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="New Character", command=self.newAlly)
        file.add_command(label="Save")
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Undo")
        edit.add_command(label="Redo")
        menu.add_cascade(label="Edit", menu=edit)

    def showImg(self):
        load = Image.Image.resize(Image.open("yasser.png"), size=(100,100))
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def showTxt(self):
        text = Label(self, text="Noooooo!")
        text.pack()

    def newAlly(self):
        exit()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("1200x700")

app = Window(root)

root.mainloop()
