from Tkinter import Tk
import Tkinter

class Window(Tk):
    def __init__(self):
        Tkinter.Tk.__init__(self)
        self.login_windows()

    def login_windows(self):
        self.title('ssf')
        self.image_file = Tkinter.PhotoImage(file='/Users/wanghaoran/Desktop/0.gif')
        Tkinter.Label(self,image=self.image_file).pack()


a = Window()
a.mainloop()
