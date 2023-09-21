import tkinter as tk
import seswithpython as sp


def display():
    templates = sp.list_templates()
    template_names = [template['Name'] for template in templates['TemplatesMetadata']]

    window = tk.Tk()
    window.geometry("800x600")

    # Create a label for the heading
    heading_label = tk.Label(window, text="Templates", font=("Helvetica", 16))
    heading_label.pack(pady=10)  # Add some padding

    # Create a text box to display the template names
    text_box = tk.Text(window, height=10, width=40)
    text_box.place(x=25,y=25)
    text_box.pack()

    # Insert the template names into the text box
    for name in template_names:
        text_box.insert(tk.END, name + "\n")

    window.mainloop()


# Call the display_templates function to display template names
#display()
