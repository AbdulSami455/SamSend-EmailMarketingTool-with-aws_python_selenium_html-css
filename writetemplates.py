import tkinter as tk
import seswithpython as sp

def write():
    window=tk.Tk()
    window.geometry("800x600")
    templates = sp.list_templates()
    print(templates['names'])

    # Insert template names into the text box


    window.mainloop()