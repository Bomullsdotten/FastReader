import Tkinter
import FastReader as FR
#C:\Users\Sondre\Documents\2nd grade\Computer Networking.txt

class MainFrame:
    def __init__(self):
        self.mainWindow = Tkinter.Tk()
        self.topFrame = Tkinter.Frame()
        self.botFrame = Tkinter.Frame()

        self.pathLabel = Tkinter.Label(self.topFrame, text='Enter full pathname:')
        self.pathEntry = Tkinter.Entry(self.topFrame, width = 10)

        self.pathLabel.pack(side='left')
        self.pathEntry.pack(side='left')

        self.start = Tkinter.Button(self.botFrame, text = 'Start', command = lambda: self.convert(self.mainWindow))
        self.quit = Tkinter.Button(self.botFrame, text = 'Quit', command = self.mainWindow.destroy)

        self.start.pack(side = 'left')
        self.quit.pack(side='left')

        self.topFrame.pack()
        self.botFrame.pack()

        Tkinter.mainloop()

    def convert(self, root):
        print 'hmm'
        path = self.pathEntry.get()
        fr = FR.FastReader(path, root)
        print 'lol'
t = MainFrame()
