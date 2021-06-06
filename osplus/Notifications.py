from tkinter import *


class Normal(object):
    def __init__(self, title: str, msg: str, accept, cancel, help=None):
        """Defines a Notification using tkinter. accept, cancel and help (optional) need a function to be called on these events"""
        self.title = title
        self.msg = msg,
        self.accept = accept
        self.cancel = cancel
        self.help = help
        self.window = None

    def show(self):
        """Shows the defined Notification and triggers the specified events"""
        self.window = Tk()
        self.window.title(self.title)
        self.window.wm_attributes("-topmost", 1)
        Label(self.window, text=self.msg).pack()
        Button(self.window, text='OK', command=self.accpeted)
        Button(self.window, text='Cancel', command=self.cancelled)
        if self.help is not None:
            Button(self.window, text='Help', command=self.helped)
        self.window.mainloop()

    def accpeted(self):
        self.window.destroy()
        self.accept()

    def cancelled(self):
        self.window.destroy()
        self.cancel()

    def helped(self):
        self.help()

    def dismiss(self):
        """Dismisses the Notification manually"""
        self.window.destroy()
