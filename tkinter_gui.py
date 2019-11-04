import tkinter as tk
from tkinter import font as tkfont
import pyductivity as pd

h = 650
w = 300


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Roboto', size=18, weight="bold", slant="italic")
        self.text_font = tkfont.Font(family='Droid Sans', size=12)
        self.button_font = tkfont.Font(family='Verdana', size=12)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        canvas = tk.Canvas(self, height=h, width=w)
        canvas.pack()
        container = tk.Frame(self, bg='#34b3b3')
        container.place(relwidth=1, relheight=1)
        # container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (LandingPage, CategoryInputPage, ActivityInputPage, LuckyPage, OddsViewPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LandingPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class LandingPage(tk.Frame):  # todo button image

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pyductivity", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label = tk.Label(self, text="This app utilizes operant conditioning to help you be more productive.",
                         font=controller.text_font, wraplength=300)
        label.pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Start", command=lambda: controller.show_frame("CategoryInputPage"),
                            font=controller.button_font).pack()
        # button1.config = (image=tk.PhotoImage(file='play_button.png'))
        button2 = tk.Button(self, text="I'm Feeling Lucky",
                            command=lambda: controller.show_frame("LuckyPage"), font=controller.button_font)
        button2.pack()
        button3 = tk.Button(self, text="View Odds",
                            command=lambda: controller.show_frame("OddsViewPage"), font=controller.button_font)
        button3.pack()


class CategoryInputPage(
    tk.Frame):  # todo append text boxes and display dict in real time, append text box popup, or directly edit dict

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pyductivity", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Category Input", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Please enter categories",
                         font=controller.text_font, wraplength=300)
        label.pack(side="top", fill="x", pady=10)
        category_entry = tk.Entry(self).pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Please enter chance parameter",
                         font=controller.text_font, wraplength=300)
        label.pack(side="top", fill="x", pady=10)
        parameter_entry = tk.Entry(self).pack(side="top", fill="x", pady=10)
        button1 = tk.Button(self, text="Home",
                            command=lambda: controller.show_frame("LandingPage"), font=controller.button_font).pack()
        button1 = tk.Button(self, text="Submit",
                            command=lambda: pd.Category.user_input(), font=controller.button_font).pack()
        button2 = tk.Button(self, text="Input Activity",
                            command=lambda: controller.show_frame("LandingPage"), font=controller.button_font).pack()


class ActivityInputPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pyductivity", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("LandingPage"), font=controller.button_font).pack()


class LuckyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pyductivity", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="I'm feeling lucky", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("LandingPage"), font=controller.button_font).pack()


class OddsViewPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pyductivity", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label = tk.Label(self, text="Odds View Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Home",
                           command=lambda: controller.show_frame("LandingPage"), font=controller.button_font)
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
