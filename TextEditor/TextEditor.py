import tkinter as Tk
from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText

class NotePad:

    def __init__(self,root):
        self.root = root
        #creating a menubar
        menubar = Menu(root)
        filemenu = Menu(menubar,teroff=0)
        filemenu.add_command(label="New",command=self.new_file)
        filemenu.add_command(label="Open",command=self.open_file)
        filemenu.add_command(label="Save",command=self.save)
        filemenu.add_command(label="Save as",command=self.save_as)
        filemenu.add_separator()
        filemenu.add_command(label="Exit",command=root.quit)
        menubar.add_cascade(label="File",menu=filemenu)
        self.root.config(menu=menubar)

        self.textarea = ScrolledText(self.root,font=('arial', 14),undo=True,wrap = WORD)
        self.textarea.place(relwidth=1, relheight=1)

    def new_file(self,*args):
        self.textarea.delete(1.0,END)
        self.filename = None

    def open_file(self,*args):
        self.filename = askopenfilename(
            defaultextension = ".txt",
            filetypes=[('All Files','*.*'),
                        ('Text Files','*.txt'),
                        ('Python Scripts','*.py'),
                        ('Javascript','*.js')])

        if self.filename:
            self.textarea.delete(1.0,END)
            with open(self.filename,"r") as f:
                self.textarea.insert(1.0,f.read())

    def save(self,*args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0,END)
                with open(self.filename,'w') as f:
                    f.write(textarea_content)
            except Exception as e:
                print(e)

        else:
            self.save_as()

    def save_as(self,*args):
        try:
            new_file = asksaveasfilename(
                initialfile = "Untitled.txt",
                defaultextension = ".txt",
                filetypes=[('All Files','*.*'),
                        ('Text Files','*.txt'),
                        ('Python Scripts','*.py'),
                        ('Javascript','*.js')])
            textarea_content = self.textarea.get(1.0,END)
            with open(new_file,'w') as f:
                f.write(textarea_content)

        except Exception as e:
            print(e)




if __name__ == "main":
    root = Tk()
    root.title("NotePad with Python")
    root.geometry("500x500")
    root.configure(bg="white")
    NotePad(root)
    root.mainloop()


