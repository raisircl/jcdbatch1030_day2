import tkinter as tk

window=tk.Tk()
window.title("Welcome to Tkinter")
window.geometry("600x400")
window.configure(bg="lightblue")
label=tk.Label(window,text="Welcome to Windows App",fg="red",bg="lightblue",font=("Arial",24))
label.pack(padx=0)
window.mainloop()
