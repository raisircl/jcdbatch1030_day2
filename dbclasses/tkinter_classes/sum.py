import tkinter as tk

def btn_click():
    n1=int(txtn1.get())
    n2=int(txtn2.get())
    sum=n1+n2
    #print(f"Sum of {n1} and {n2} is: {sum}")
    lblresult.config(text=f"Sum of {n1} and {n2} is: {sum}")

window=tk.Tk()
window.title("Sum Calculator")
window.geometry("600x400")

lbln1=tk.Label(window,text="Enter first number:")
lbln1.grid(row=0,column=0,padx=10,pady=10)
txtn1=tk.Entry(window,width=30) 
txtn1.grid(row=0,column=1,padx=10,pady=10)

lbln2=tk.Label(window,text="Enter second number:")
lbln2.grid(row=1,column=0,padx=10,pady=10)
txtn2=tk.Entry(window,width=30)
txtn2.grid(row=1,column=1,padx=10,pady=10)

btnsum=tk.Button(window,text="Calculate",command=btn_click)
btnsum.grid(row=2,column=0,padx=10,pady=10)

lblresult=tk.Label(window,text="Result will be displayed here")
lblresult.grid(row=2,column=1,padx=10,pady=10)

window.mainloop()
