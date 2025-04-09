from tkinter import *
from tkinter.ttk import Progressbar
from progressTimer import start
import pyperclip
import time
import os
import sys

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        # Fallback to the current directory if not bundled
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


import passwordGenerator

icon_path = resource_path("appicon.ico")

tk = Tk()
tk.geometry("420x420")
tk.resizable(False, False)
tk.iconbitmap(icon_path)
tk.eval('tk::PlaceWindow . center')
tk.title("Password Generator")



def copyToClipboard(text):
    pyperclip.copy(text)
    copyToClipboard.outputText = Label(passwordWindow, text="Successfully copied to window!")
    copyToClipboard.outputText.pack()
    passwordWindow.update()
    passwordWindow.after(2500)
    passwordWindow.after(1000, close_window())

def close_window():
    passwordWindow.quit()   # Stop the Tkinter main loop
    passwordWindow.destroy()  # Destroy the window (closes it)

def on_progress_complete():
    tk.destroy()
    global passwordWindow
    passwordWindow = Tk()
    passwordWindow.geometry("250x150")
    passwordWindow.iconbitmap(icon_path)
    passwordWindow.eval('tk::PlaceWindow . center')
    passwordWindow.resizable(False, False)
    passwordWindow.title("Password Output")

    titleLabel = Label(passwordWindow, text="Generated Password: ")
    titleLabel.pack()

    passwordLabel = Label(passwordWindow, text=password,
                          font=('Arial', 18, 'bold'),
                          relief=GROOVE)
    passwordLabel.pack()

    copyButton = Button(passwordWindow, text="copy", command=lambda: copyToClipboard(passwordLabel.cget("text")))
    copyButton.pack()




    passwordWindow.mainloop()


def on_enter_name(event):
    global name
    name = namebox.get()
    namebox.config(state=DISABLED)



    global secondbox, secondLabel
    secondLabel = Label(tk, text="Second Name:")
    secondLabel.pack()
    secondbox = Entry(tk)
    secondbox.pack()
    secondbox.focus_set()
    secondbox.bind("<Return>", getBirth)

def getBirth(event):
    global secondName
    secondName = secondbox.get()
    secondbox.config(state=DISABLED)


    global birthbox, birthLabel
    birthLabel = Label(tk, text="Year Born:")
    birthLabel.pack()
    birthbox = Entry(tk)
    birthbox.pack()
    birthbox.focus_set()
    birthbox.bind("<Return>", formSubmit)

def formSubmit(event):
    global birthDate
    birthDate = birthbox.get()
    birthbox.config(state=DISABLED)

    global password
    password = passwordGenerator.generatePassword(name, secondName, birthDate)
    submitButton.forget()

    global progressBar
    bar = Progressbar(tk, orient=HORIZONTAL, length=300)
    bar.pack(pady=10)
    progress = start(bar, tk, callback=on_progress_complete)



def getDetails():
    global namebox
    global nameLabel
    nameLabel = Label(tk, text="Name:")
    nameLabel.pack()
    namebox = Entry(tk)
    namebox.pack()
    namebox.focus_set()
    namebox.bind("<Return>", on_enter_name)



label = Label(tk, text="Password Generator", font=('Arial', 30, 'bold'))
label.pack()

submitButton = Button(tk, text="Generate Password", command=getDetails)
submitButton.pack()

tk.mainloop()
