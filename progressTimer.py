import random
import time
import tkinter.ttk

def start(bar, window, x=0, tasks=10, callback=None):
    if x < tasks:
        bar['value'] += 100 / tasks
        window.update_idletasks()
        window.after(200, start, bar, window, x + 1, tasks, callback)
    else:
        if callback:
            callback()


