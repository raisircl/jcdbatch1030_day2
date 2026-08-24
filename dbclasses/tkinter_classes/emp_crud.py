import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from datetime import date
import sqlite3


# ---------------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------------
def connect_db():
    """
    Connect to SQLite database.
    """
    return sqlite3.connect("payroll.db")


# ---------------------------------------------------------
# CREATE EMPLOYEE TABLE
# ---------------------------------------------------------
def create_table():
    """
    Create tblemp table if it does not already exist.
    """

    con = connect_db()
    cur = con.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS tblemp
        (
            empno INTEGER PRIMARY KEY,
            ename TEXT NOT NULL,
            job TEXT NOT NULL,
            salary REAL NOT NULL,
            hiredate TEXT NOT NULL,
            dno INTEGER NOT NULL
        )
    """)

    con.commit()
    con.close()


# ---------------------------------------------------------
# DEPARTMENT DICTIONARY
# ---------------------------------------------------------

# Example:
# {
#     "Accounts": 10,
#     "Sales": 20,
#     "HR": 30
# }

department_dict = {}


# ---------------------------------------------------------
# LOAD DEPARTMENTS
# ---------------------------------------------------------
def load_departments():
    """
    Read department number and department name.

    Display department name in combo box,
    but store department number in employee table.
    """

    global department_dict

    try:
        con = connect_db()
        cur = con.cursor()

        cur.execute("""
            SELECT dno, dname
            FROM tbldept
            ORDER BY dname
        """)

        rows = cur.fetchall()

        con.close()

        department_dict = {}

        department_names = []

        for row in rows:

            dno = row[0]
            dname = row[1]

            # Department name -> Department number
            department_dict[dname] = dno

            department_names.append(dname)

        # Show department names in combo box
        cmb_dno["values"] = department_names

    except sqlite3.Error as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# CLEAR FORM
# ---------------------------------------------------------
def clear_form():
    """
    Clear all input fields.
    """

    txt_empno.delete(0, tk.END)

    txt_ename.delete(0, tk.END)

    txt_job.delete(0, tk.END)

    txt_salary.delete(0, tk.END)

    # Set current date
    txt_hiredate.set_date(date.today())

    # Clear department combo
    cmb_dno.set("")

    txt_empno.focus()


# ---------------------------------------------------------
# READ / SHOW DATA
# ---------------------------------------------------------
def fetch_data():
    """
    Read all employee records
    and display them in the grid.
    """

    try:

        con = connect_db()
        cur = con.cursor()

        cur.execute("""
            SELECT empno,
                   ename,
                   job,
                   salary,
                   hiredate,
                   dno
            FROM tblemp
        """)

        rows = cur.fetchall()

        con.close()

        # Clear old grid rows
        for item in grid.get_children():
            grid.delete(item)

        # Add database rows to grid
        for row in rows:
            grid.insert(
                "",
                tk.END,
                values=row
            )

    except sqlite3.Error as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# INSERT
# ---------------------------------------------------------
def insert_data():
    """
    Insert a new employee into tblemp.
    """

    empno = txt_empno.get().strip()

    ename = txt_ename.get().strip()

    job = txt_job.get().strip()

    salary = txt_salary.get().strip()

    hiredate = txt_hiredate.get()

    # Combo box gives department NAME
    department_name = cmb_dno.get().strip()


    # -----------------------------------------------------
    # CHECK EMPTY FIELDS
    # -----------------------------------------------------

    if (
        empno == "" or
        ename == "" or
        job == "" or
        salary == "" or
        department_name == ""
    ):

        messagebox.showwarning(
            "Missing Data",
            "Please enter all fields."
        )

        return


    # -----------------------------------------------------
    # CHECK EMPLOYEE NUMBER
    # -----------------------------------------------------

    if not empno.isdigit():

        messagebox.showwarning(
            "Invalid Data",
            "Employee number must be numeric."
        )

        return


    # -----------------------------------------------------
    # CHECK SALARY
    # -----------------------------------------------------

    try:

        salary_value = float(salary)

    except ValueError:

        messagebox.showwarning(
            "Invalid Data",
            "Salary must be numeric."
        )

        return


    # -----------------------------------------------------
    # GET DEPARTMENT NUMBER
    # -----------------------------------------------------

    dno = department_dict[department_name]


    # -----------------------------------------------------
    # INSERT INTO DATABASE
    # -----------------------------------------------------

    try:

        con = connect_db()
        cur = con.cursor()

        sql = """
            INSERT INTO tblemp
            (
                empno,
                ename,
                job,
                salary,
                hiredate,
                dno
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """

        cur.execute(
            sql,
            (
                empno,
                ename,
                job,
                salary_value,
                hiredate,
                dno
            )
        )

        con.commit()

        con.close()


        messagebox.showinfo(
            "Success",
            "Employee added successfully."
        )


        fetch_data()

        clear_form()


    except sqlite3.IntegrityError:

        messagebox.showerror(
            "Error",
            "Employee number already exists."
        )


    except sqlite3.Error as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# UPDATE
# ---------------------------------------------------------
def update_data():
    """
    Update employee details
    using employee number.
    """

    empno = txt_empno.get().strip()

    ename = txt_ename.get().strip()

    job = txt_job.get().strip()

    salary = txt_salary.get().strip()

    hiredate = txt_hiredate.get()

    department_name = cmb_dno.get().strip()


    # -----------------------------------------------------
    # CHECK EMPLOYEE NUMBER
    # -----------------------------------------------------

    if empno == "":

        messagebox.showwarning(
            "Select Record",
            "Please select a record to update."
        )

        return


    # -----------------------------------------------------
    # CHECK EMPTY FIELDS
    # -----------------------------------------------------

    if (
        ename == "" or
        job == "" or
        salary == "" or
        department_name == ""
    ):

        messagebox.showwarning(
            "Missing Data",
            "Please enter all employee details."
        )

        return


    # -----------------------------------------------------
    # CHECK SALARY
    # -----------------------------------------------------

    try:

        salary_value = float(salary)

    except ValueError:

        messagebox.showwarning(
            "Invalid Data",
            "Salary must be numeric."
        )

        return


    # -----------------------------------------------------
    # GET DEPARTMENT NUMBER
    # -----------------------------------------------------

    dno = department_dict[department_name]


    # -----------------------------------------------------
    # UPDATE DATABASE
    # -----------------------------------------------------

    try:

        con = connect_db()
        cur = con.cursor()

        sql = """
            UPDATE tblemp

            SET ename = ?,
                job = ?,
                salary = ?,
                hiredate = ?,
                dno = ?

            WHERE empno = ?
        """

        cur.execute(
            sql,
            (
                ename,
                job,
                salary_value,
                hiredate,
                dno,
                empno
            )
        )

        con.commit()

        con.close()


        messagebox.showinfo(
            "Success",
            "Employee updated successfully."
        )


        fetch_data()

        clear_form()


    except sqlite3.Error as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# DELETE
# ---------------------------------------------------------
def delete_data():
    """
    Delete employee using employee number.
    """

    empno = txt_empno.get().strip()


    if empno == "":

        messagebox.showwarning(
            "Select Record",
            "Please select a record to delete."
        )

        return


    answer = messagebox.askyesno(
        "Confirm Delete",
        "Are you sure you want to delete this employee?"
    )


    if answer == False:
        return


    try:

        con = connect_db()
        cur = con.cursor()

        cur.execute(
            """
            DELETE FROM tblemp
            WHERE empno = ?
            """,
            (empno,)
        )

        con.commit()

        con.close()


        messagebox.showinfo(
            "Success",
            "Employee deleted successfully."
        )


        fetch_data()

        clear_form()


    except sqlite3.Error as e:

        messagebox.showerror(
            "Database Error",
            str(e)
        )


# ---------------------------------------------------------
# GRID ROW SELECTION
# ---------------------------------------------------------
def select_row(event):
    """
    When a row is selected in the grid,
    show that row's values in the form.
    """

    selected_item = grid.focus()


    if selected_item == "":
        return


    row = grid.item(selected_item)

    values = row["values"]


    if not values:
        return


    # -----------------------------------------------------
    # CLEAR FORM
    # -----------------------------------------------------

    txt_empno.delete(0, tk.END)

    txt_ename.delete(0, tk.END)

    txt_job.delete(0, tk.END)

    txt_salary.delete(0, tk.END)


    # -----------------------------------------------------
    # PUT VALUES INTO FORM
    # -----------------------------------------------------

    txt_empno.insert(
        0,
        values[0]
    )

    txt_ename.insert(
        0,
        values[1]
    )

    txt_job.insert(
        0,
        values[2]
    )

    txt_salary.insert(
        0,
        values[3]
    )


    # -----------------------------------------------------
    # HIRE DATE
    # -----------------------------------------------------

    txt_hiredate.set_date(
        values[4]
    )


    # -----------------------------------------------------
    # DEPARTMENT
    # -----------------------------------------------------

    # Employee table contains department number
    selected_dno = values[5]

    # Find department name
    for dname, dno in department_dict.items():

        if dno == selected_dno:

            cmb_dno.set(dname)

            break


# =========================================================
# CREATE MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Employee CRUD - SQLite"
)

root.geometry(
    "950x650"
)


# =========================================================
# TITLE
# =========================================================

lbl_title = tk.Label(
    root,
    text="Employee Management",
    font=("Arial", 20, "bold")
)

lbl_title.pack(
    pady=10
)


# =========================================================
# FORM
# =========================================================

form_frame = tk.Frame(root)

form_frame.pack(
    pady=10
)


# ---------------------------------------------------------
# EMPLOYEE NUMBER
# ---------------------------------------------------------

tk.Label(
    form_frame,
    text="Employee No:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


txt_empno = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)


txt_empno.grid(
    row=0,
    column=1,
    padx=10,
    pady=8
)


# ---------------------------------------------------------
# EMPLOYEE NAME
# ---------------------------------------------------------

tk.Label(
    form_frame,
    text="Employee Name:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


txt_ename = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)


txt_ename.grid(
    row=1,
    column=1,
    padx=10,
    pady=8
)


# ---------------------------------------------------------
# JOB
# ---------------------------------------------------------

tk.Label(
    form_frame,
    text="Job:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


txt_job = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)


txt_job.grid(
    row=2,
    column=1,
    padx=10,
    pady=8
)


# ---------------------------------------------------------
# SALARY
# ---------------------------------------------------------

tk.Label(
    form_frame,
    text="Salary:",
    font=("Arial", 12)
).grid(
    row=3,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


txt_salary = tk.Entry(
    form_frame,
    font=("Arial", 12),
    width=30
)


txt_salary.grid(
    row=3,
    column=1,
    padx=10,
    pady=8
)


# ---------------------------------------------------------
# HIRE DATE
# ---------------------------------------------------------

tk.Label(
    form_frame,
    text="Hire Date:",
    font=("Arial", 12)
).grid(
    row=4,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


txt_hiredate = DateEntry(
    form_frame,
    font=("Arial", 12),
    width=28,
    date_pattern="yyyy-mm-dd"
)


txt_hiredate.grid(
    row=4,
    column=1,
    padx=10,
    pady=8
)


# ---------------------------------------------------------
# DEPARTMENT
# ---------------------------------------------------------

tk.Label(
    form_frame,
    text="Department:",
    font=("Arial", 12)
).grid(
    row=5,
    column=0,
    padx=10,
    pady=8,
    sticky="w"
)


cmb_dno = ttk.Combobox(
    form_frame,
    font=("Arial", 12),
    width=28,
    state="readonly"
)


cmb_dno.grid(
    row=5,
    column=1,
    padx=10,
    pady=8
)


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(root)

button_frame.pack(
    pady=10
)


# ADD
tk.Button(
    button_frame,
    text="Add",
    width=10,
    command=insert_data
).grid(
    row=0,
    column=0,
    padx=5
)


# UPDATE
tk.Button(
    button_frame,
    text="Update",
    width=10,
    command=update_data
).grid(
    row=0,
    column=1,
    padx=5
)


# DELETE
tk.Button(
    button_frame,
    text="Delete",
    width=10,
    command=delete_data
).grid(
    row=0,
    column=2,
    padx=5
)


# CLEAR
tk.Button(
    button_frame,
    text="Clear",
    width=10,
    command=clear_form
).grid(
    row=0,
    column=3,
    padx=5
)


# REFRESH
tk.Button(
    button_frame,
    text="Refresh",
    width=10,
    command=fetch_data
).grid(
    row=0,
    column=4,
    padx=5
)


# =========================================================
# GRID / TREEVIEW
# =========================================================

grid_frame = tk.Frame(root)


grid_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=10
)


grid = ttk.Treeview(
    grid_frame,
    columns=(
        "empno",
        "ename",
        "job",
        "salary",
        "hiredate",
        "dno"
    ),
    show="headings"
)


# ---------------------------------------------------------
# GRID HEADINGS
# ---------------------------------------------------------

grid.heading(
    "empno",
    text="Employee No"
)


grid.heading(
    "ename",
    text="Employee Name"
)


grid.heading(
    "job",
    text="Job"
)


grid.heading(
    "salary",
    text="Salary"
)


grid.heading(
    "hiredate",
    text="Hire Date"
)


grid.heading(
    "dno",
    text="Department No"
)


# ---------------------------------------------------------
# GRID COLUMN SIZES
# ---------------------------------------------------------

grid.column(
    "empno",
    width=100,
    anchor="center"
)


grid.column(
    "ename",
    width=170
)


grid.column(
    "job",
    width=130
)


grid.column(
    "salary",
    width=100,
    anchor="center"
)


grid.column(
    "hiredate",
    width=120,
    anchor="center"
)


grid.column(
    "dno",
    width=120,
    anchor="center"
)


# ---------------------------------------------------------
# SCROLLBAR
# ---------------------------------------------------------

scrollbar = ttk.Scrollbar(
    grid_frame,
    orient="vertical",
    command=grid.yview
)


grid.configure(
    yscrollcommand=scrollbar.set
)


grid.pack(
    side="left",
    fill="both",
    expand=True
)


scrollbar.pack(
    side="right",
    fill="y"
)


# ---------------------------------------------------------
# GRID ROW SELECTION
# ---------------------------------------------------------

grid.bind(
    "<<TreeviewSelect>>",
    select_row
)


# =========================================================
# START PROGRAM
# =========================================================

# Create employee table
create_table()


# Load department names into combo box
load_departments()


# Show employee records
fetch_data()


# Cursor starts at employee number
txt_empno.focus()


# Start Tkinter
root.mainloop()