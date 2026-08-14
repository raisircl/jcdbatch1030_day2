import tkinter as tk
from tkinter import ttk
def btn_click():
    print(chkpython.state())
    selected_languages=[]
    if chkpython.instate(['selected']):
        selected_languages.append("Python")
    if chkjava.instate(['selected']):
        selected_languages.append("Java")
    if chkcpp.instate(['selected']):
        selected_languages.append("C++")
    lblresult.config(text=f"Selected languages: {', '.join(selected_languages)}")
    
window=tk.Tk()
window.title("CheckBox Example")
lbltitle=ttk.Label(window,text="Select your favorite programming languages:")
lbltitle.pack()
chkpython=ttk.Checkbutton(window,text="Python")
chkpython.pack()
chkjava=ttk.Checkbutton(window,text="Java")
chkjava.pack()
chkcpp=ttk.Checkbutton(window,text="C++")
chkcpp.pack()
btnsubmit=ttk.Button(window,text="Submit",command=btn_click)
btnsubmit.pack()
lblresult=ttk.Label(window,text="Selected languages will be displayed here")
lblresult.pack()
window.mainloop()