import tkinter as tk

def say_hello():
    name=txtname.get()
    print(f"Hello, {name}!")
    
window=tk.Tk()
window.title("Entry Form")
window.geometry("600x400")

lblname=tk.Label(window,text="Enter your name:")
lblname.pack(pady=10)
txtname=tk.Entry(window, width=30)
txtname.pack(pady=10)

btnsubmit=tk.Button(window,text="Save",command=say_hello)
btnsubmit.pack(pady=10)
window.mainloop()