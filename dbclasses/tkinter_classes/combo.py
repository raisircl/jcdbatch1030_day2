import tkinter as tk
from tkinter import ttk

# 1. Define the dictionary with courses and fees
COURSE_FEES = {
    "Python Programming": "₹5,000",
    "Data Science BootCamp": "₹12,000",
    "Web Development (MERN)": "₹8,500",
    "Machine Learning Essentials": "₹15,000",
    "Cyber Security Basics": "₹7,000"
}

window = tk.Tk()
window.title("Course Fee Viewer")
window.geometry("400x250")

# Function triggered automatically when an item is selected
def on_course_select(event):
    # Get the currently selected course text
    selected_course = combo_courses.get()
    
    # Look up the fee from the dictionary
    fee = COURSE_FEES.get(selected_course, "N/A")
    
    # Update the label text
    lbl_fee_val.config(text=fee)

# --- Layout Elements ---

# 1. Title Label
lbl_title = ttk.Label(window, text="Select Course to View Fee", font=("Arial", 14, "bold"))
lbl_title.pack(pady=20)

# 2. Dropdown List (Combobox)
# We load the dictionary keys directly into the values parameter
combo_courses = ttk.Combobox(window, values=list(COURSE_FEES.keys()), state="readonly", width=30)
combo_courses.set("--- Choose a Course ---")  # Default placeholder text
combo_courses.pack(pady=10)

# 3. Bind the selection event to our function
# '<<ComboboxSelected>>' triggers immediately upon a user click
combo_courses.bind("<<ComboboxSelected>>", on_course_select)

# 4. Results Framework (Labels)
frame_result = ttk.Frame(window)
frame_result.pack(pady=20)

lbl_fee_text = ttk.Label(frame_result, text="Course Fee: ", font=("Arial", 11))
lbl_fee_text.pack(side="left")

lbl_fee_val = ttk.Label(frame_result, text="—", font=("Arial", 12, "bold"), foreground="green")
lbl_fee_val.pack(side="left")

window.mainloop()
