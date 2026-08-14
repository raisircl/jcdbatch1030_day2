import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Fee Calculator")
window.geometry("400x450")

# Separate tracking variables for each group
gender_var = tk.StringVar(value="None")
category_var = tk.StringVar(value="None")

def btn_click():
    gender = gender_var.get()
    category = category_var.get()
    
    # 1. Validation check if user forgot to select an option
    if gender == "None" or category == "None":
        lbl_result.config(text="Please select both Gender and Category!", foreground="red")
        return

    # 2. Evaluate the dynamic fee logic
    fee = 0
    if category == "General" and gender == "Male":
        fee = 1000
    elif category == "General" and gender == "Female":
        fee = 600
    elif category == "OBC" and gender == "Male":
        fee = 800
    elif category == "OBC" and gender == "Female":
        fee = 500
    elif category == "SC" and gender == "Male":
        fee = 500
    elif category == "SC" and gender == "Female":
        fee = 100

    # 3. Display the calculation to the user
    lbl_result.config(text=f"Total Fee: ₹{fee}", foreground="black")

# --- Gender Group ---
lblframe_gender = ttk.LabelFrame(window, text="Select your gender:")
lblframe_gender.pack(padx=10, pady=10, fill="both", expand="yes")

rblmale = ttk.Radiobutton(lblframe_gender, text="Male", value="Male", variable=gender_var)
rblmale.pack(anchor="w", padx=10, pady=2)
rbfemale = ttk.Radiobutton(lblframe_gender, text="Female", value="Female", variable=gender_var)
rbfemale.pack(anchor="w", padx=10, pady=2)

# --- Category Group ---
lblframe_category = ttk.LabelFrame(window, text="Select your category:")
lblframe_category.pack(padx=10, pady=10, fill="both", expand="yes")

rblgeneral = ttk.Radiobutton(lblframe_category, text="General", value="General", variable=category_var)
rblgeneral.pack(anchor="w", padx=10, pady=2)
rblobc = ttk.Radiobutton(lblframe_category, text="OBC", value="OBC", variable=category_var)
rblobc.pack(anchor="w", padx=10, pady=2)
rbsc = ttk.Radiobutton(lblframe_category, text="SC", value="SC", variable=category_var)
rbsc.pack(anchor="w", padx=10, pady=2)

# --- Submit Button ---
btnsubmit = ttk.Button(window, text="Calculate Fee", command=btn_click)
btnsubmit.pack(pady=10)

# --- Result Display Label ---
lbl_result = ttk.Label(window, text="", font=("Arial", 12, "bold"))
lbl_result.pack(pady=10)

window.mainloop()
