import tkinter as tk
from tkinter import filedialog

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is None:
        return
    text = text_widget.get("1.0", "end-1c")
    file.write(text)
    file.close()
    
def open_file():
    file = filedialog.askopenfile(mode='r')
    if file is None:
        return
    text = file.read()
    text_widget.delete('1.0', tk.END)
    text_widget.insert('1.0', text)
    file.close()
    
def new_file():
    text_widget.delete('1.0', tk.END)

root = tk.Tk()
root.title("Notepad")

# Creating a Menu Bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# File Menu
file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Edit Menu
edit_menu = tk.Menu(menubar)
menubar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: text_widget.cut())
edit_menu.add_command(label="Copy", command=lambda: text_widget.copy())
edit_menu.add_command(label="Paste", command=lambda: text_widget.paste())



# Text Widget
text_widget = tk.Text(root)
text_widget.pack()

root.mainloop()