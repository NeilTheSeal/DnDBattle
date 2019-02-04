import tkinter as tk
from PIL import Image, ImageTk
import charBuilder

HEADER_FONT = ("Optima", 24, "italic")
SMALL_FONT = ("Arial", 16)

class MainProg(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.title("DnD Battle Builder")

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="DnD Battle Builder", font=HEADER_FONT)
        label.grid(row=0, column=0, padx=500, pady=[200,50])
        print(label.grid_info())

        newbattleButton = tk.Button(self, text="new battle", height="2", width="9", font=SMALL_FONT,
                                    command=lambda: controller.show_frame(PageOne))
        newbattleButton.grid(row=1, column=0, pady=[0,10])

        loadbattleButton = tk.Button(self, text="load battle", height="2", width="9", font=SMALL_FONT)
        loadbattleButton.grid(row=3, column=0)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 1", font=HEADER_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Start Page", font=SMALL_FONT,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 2", font=SMALL_FONT,
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 2", font=HEADER_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Start Page", font=SMALL_FONT,
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 1", font=SMALL_FONT,
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

app = MainProg()
app.geometry("1200x700")
app.mainloop()
