import tkinter as tk
from tkinter import ttk, messagebox

# ============================================================
# COUNTRY DATA
# ============================================================
def get_countries():
    # get data from countries table in database
    countries = [
        {"id": 1, "name": "India"},
        {"id": 2, "name": "USA"}
    ]
    return countries




# ============================================================
# STATE DATA
# country_id tells which country the state belongs to
# ============================================================

states = [
    # India
    {"id": 1, "country_id": 1, "name": "Haryana"},
    {"id": 2, "country_id": 1, "name": "Punjab"},
    {"id": 3, "country_id": 1, "name": "Rajasthan"},
    {"id": 4, "country_id": 1, "name": "Uttar Pradesh"},
    {"id": 5, "country_id": 1, "name": "Maharashtra"},

    # USA
    {"id": 6, "country_id": 2, "name": "California"},
    {"id": 7, "country_id": 2, "name": "Texas"},
    {"id": 8, "country_id": 2, "name": "Florida"},
    {"id": 9, "country_id": 2, "name": "New York"},
    {"id": 10, "country_id": 2, "name": "Illinois"}
]


# ============================================================
# CITY DATA
# state_id tells which state the city belongs to
# ============================================================

cities = [

    # --------------------------------------------------------
    # Haryana - State ID 1
    # --------------------------------------------------------
    {"id": 1, "state_id": 1, "name": "Gurugram"},
    {"id": 2, "state_id": 1, "name": "Faridabad"},
    {"id": 3, "state_id": 1, "name": "Panipat"},
    {"id": 4, "state_id": 1, "name": "Ambala"},
    {"id": 5, "state_id": 1, "name": "Karnal"},
    {"id": 6, "state_id": 1, "name": "Hisar"},
    {"id": 7, "state_id": 1, "name": "Rohtak"},
    {"id": 8, "state_id": 1, "name": "Sonipat"},
    {"id": 9, "state_id": 1, "name": "Kurukshetra"},
    {"id": 10, "state_id": 1, "name": "Sirsa"},

    # --------------------------------------------------------
    # Punjab - State ID 2
    # --------------------------------------------------------
    {"id": 11, "state_id": 2, "name": "Ludhiana"},
    {"id": 12, "state_id": 2, "name": "Amritsar"},
    {"id": 13, "state_id": 2, "name": "Jalandhar"},
    {"id": 14, "state_id": 2, "name": "Patiala"},
    {"id": 15, "state_id": 2, "name": "Bathinda"},
    {"id": 16, "state_id": 2, "name": "Mohali"},
    {"id": 17, "state_id": 2, "name": "Pathankot"},
    {"id": 18, "state_id": 2, "name": "Moga"},
    {"id": 19, "state_id": 2, "name": "Hoshiarpur"},
    {"id": 20, "state_id": 2, "name": "Firozpur"},

    # --------------------------------------------------------
    # Rajasthan - State ID 3
    # --------------------------------------------------------
    {"id": 21, "state_id": 3, "name": "Jaipur"},
    {"id": 22, "state_id": 3, "name": "Jodhpur"},
    {"id": 23, "state_id": 3, "name": "Udaipur"},
    {"id": 24, "state_id": 3, "name": "Kota"},
    {"id": 25, "state_id": 3, "name": "Ajmer"},
    {"id": 26, "state_id": 3, "name": "Bikaner"},
    {"id": 27, "state_id": 3, "name": "Alwar"},
    {"id": 28, "state_id": 3, "name": "Bharatpur"},
    {"id": 29, "state_id": 3, "name": "Sikar"},
    {"id": 30, "state_id": 3, "name": "Chittorgarh"},

    # --------------------------------------------------------
    # Uttar Pradesh - State ID 4
    # --------------------------------------------------------
    {"id": 31, "state_id": 4, "name": "Lucknow"},
    {"id": 32, "state_id": 4, "name": "Kanpur"},
    {"id": 33, "state_id": 4, "name": "Agra"},
    {"id": 34, "state_id": 4, "name": "Varanasi"},
    {"id": 35, "state_id": 4, "name": "Prayagraj"},
    {"id": 36, "state_id": 4, "name": "Noida"},
    {"id": 37, "state_id": 4, "name": "Ghaziabad"},
    {"id": 38, "state_id": 4, "name": "Meerut"},
    {"id": 39, "state_id": 4, "name": "Bareilly"},
    {"id": 40, "state_id": 4, "name": "Mathura"},

    # --------------------------------------------------------
    # Maharashtra - State ID 5
    # --------------------------------------------------------
    {"id": 41, "state_id": 5, "name": "Mumbai"},
    {"id": 42, "state_id": 5, "name": "Pune"},
    {"id": 43, "state_id": 5, "name": "Nagpur"},
    {"id": 44, "state_id": 5, "name": "Nashik"},
    {"id": 45, "state_id": 5, "name": "Thane"},
    {"id": 46, "state_id": 5, "name": "Aurangabad"},
    {"id": 47, "state_id": 5, "name": "Solapur"},
    {"id": 48, "state_id": 5, "name": "Kolhapur"},
    {"id": 49, "state_id": 5, "name": "Amravati"},
    {"id": 50, "state_id": 5, "name": "Satara"},

    # --------------------------------------------------------
    # California - State ID 6
    # --------------------------------------------------------
    {"id": 51, "state_id": 6, "name": "Los Angeles"},
    {"id": 52, "state_id": 6, "name": "San Diego"},
    {"id": 53, "state_id": 6, "name": "San Jose"},
    {"id": 54, "state_id": 6, "name": "San Francisco"},
    {"id": 55, "state_id": 6, "name": "Sacramento"},
    {"id": 56, "state_id": 6, "name": "Fresno"},
    {"id": 57, "state_id": 6, "name": "Oakland"},
    {"id": 58, "state_id": 6, "name": "Long Beach"},
    {"id": 59, "state_id": 6, "name": "Bakersfield"},
    {"id": 60, "state_id": 6, "name": "Anaheim"},

    # --------------------------------------------------------
    # Texas - State ID 7
    # --------------------------------------------------------
    {"id": 61, "state_id": 7, "name": "Houston"},
    {"id": 62, "state_id": 7, "name": "Dallas"},
    {"id": 63, "state_id": 7, "name": "Austin"},
    {"id": 64, "state_id": 7, "name": "San Antonio"},
    {"id": 65, "state_id": 7, "name": "Fort Worth"},
    {"id": 66, "state_id": 7, "name": "El Paso"},
    {"id": 67, "state_id": 7, "name": "Arlington"},
    {"id": 68, "state_id": 7, "name": "Corpus Christi"},
    {"id": 69, "state_id": 7, "name": "Plano"},
    {"id": 70, "state_id": 7, "name": "Lubbock"},

    # --------------------------------------------------------
    # Florida - State ID 8
    # --------------------------------------------------------
    {"id": 71, "state_id": 8, "name": "Miami"},
    {"id": 72, "state_id": 8, "name": "Orlando"},
    {"id": 73, "state_id": 8, "name": "Tampa"},
    {"id": 74, "state_id": 8, "name": "Jacksonville"},
    {"id": 75, "state_id": 8, "name": "Tallahassee"},
    {"id": 76, "state_id": 8, "name": "Fort Lauderdale"},
    {"id": 77, "state_id": 8, "name": "St. Petersburg"},
    {"id": 78, "state_id": 8, "name": "Gainesville"},
    {"id": 79, "state_id": 8, "name": "Cape Coral"},
    {"id": 80, "state_id": 8, "name": "Clearwater"},

    # --------------------------------------------------------
    # New York - State ID 9
    # --------------------------------------------------------
    {"id": 81, "state_id": 9, "name": "New York City"},
    {"id": 82, "state_id": 9, "name": "Buffalo"},
    {"id": 83, "state_id": 9, "name": "Rochester"},
    {"id": 84, "state_id": 9, "name": "Albany"},
    {"id": 85, "state_id": 9, "name": "Syracuse"},
    {"id": 86, "state_id": 9, "name": "Yonkers"},
    {"id": 87, "state_id": 9, "name": "Ithaca"},
    {"id": 88, "state_id": 9, "name": "White Plains"},
    {"id": 89, "state_id": 9, "name": "Troy"},
    {"id": 90, "state_id": 9, "name": "Schenectady"},

    # --------------------------------------------------------
    # Illinois - State ID 10
    # --------------------------------------------------------
    {"id": 91, "state_id": 10, "name": "Chicago"},
    {"id": 92, "state_id": 10, "name": "Springfield"},
    {"id": 93, "state_id": 10, "name": "Aurora"},
    {"id": 94, "state_id": 10, "name": "Rockford"},
    {"id": 95, "state_id": 10, "name": "Naperville"},
    {"id": 96, "state_id": 10, "name": "Peoria"},
    {"id": 97, "state_id": 10, "name": "Elgin"},
    {"id": 98, "state_id": 10, "name": "Joliet"},
    {"id": 99, "state_id": 10, "name": "Evanston"},
    {"id": 100, "state_id": 10, "name": "Decatur"}
]


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Country State City Dropdown Example")
root.geometry("650x480")
root.resizable(False, False)


# ============================================================
# VARIABLES
# ============================================================

country_var = tk.StringVar()
state_var = tk.StringVar()
city_var = tk.StringVar()

country_id_var = tk.StringVar()
state_id_var = tk.StringVar()
city_id_var = tk.StringVar()


# ============================================================
# CURRENT FILTERED DATA
# ============================================================

current_states = []
current_cities = []


# ============================================================
# COUNTRY SELECTION EVENT
# ============================================================

def country_selected(event=None):

    global current_states

    selected_country_name = country_var.get()

    selected_country = None

    # Find selected country record
    for country in countries:

        if country["name"] == selected_country_name:

            selected_country = country
            break


    if selected_country is None:
        return


    # Get Country ID
    country_id = selected_country["id"]

    country_id_var.set(str(country_id))


    # Filter states by Country ID
    current_states = []

    for state in states:

        if state["country_id"] == country_id:

            current_states.append(state)


    # Prepare state names
    state_names = []

    for state in current_states:

        state_names.append(state["name"])


    # Bind states to State ComboBox
    state_combo["values"] = state_names


    # Clear old selected values
    state_var.set("")
    city_var.set("")

    state_id_var.set("")
    city_id_var.set("")

    city_combo["values"] = []


# ============================================================
# STATE SELECTION EVENT
# ============================================================

def state_selected(event=None):

    global current_cities

    selected_state_name = state_var.get()

    selected_state = None


    # Find selected state
    for state in current_states:

        if state["name"] == selected_state_name:

            selected_state = state
            break


    if selected_state is None:
        return


    # Get State ID
    state_id = selected_state["id"]

    state_id_var.set(str(state_id))


    # Filter cities by State ID
    current_cities = []

    for city in cities:

        if city["state_id"] == state_id:

            current_cities.append(city)


    # Prepare city names
    city_names = []

    for city in current_cities:

        city_names.append(city["name"])


    # Bind cities to City ComboBox
    city_combo["values"] = city_names


    # Clear previous city
    city_var.set("")
    city_id_var.set("")


# ============================================================
# CITY SELECTION EVENT
# ============================================================

def city_selected(event=None):

    selected_city_name = city_var.get()

    selected_city = None


    for city in current_cities:

        if city["name"] == selected_city_name:

            selected_city = city
            break


    if selected_city is None:
        return


    city_id_var.set(str(selected_city["id"]))


# ============================================================
# SHOW SELECTED DATA
# ============================================================

def show_data():

    if country_var.get() == "":

        messagebox.showwarning(
            "Validation",
            "Please select Country"
        )

        return


    if state_var.get() == "":

        messagebox.showwarning(
            "Validation",
            "Please select State"
        )

        return


    if city_var.get() == "":

        messagebox.showwarning(
            "Validation",
            "Please select City"
        )

        return


    message = (
        "Selected Location\n\n"
        "Country ID: " + country_id_var.get() +
        "\nCountry: " + country_var.get() +
        "\n\nState ID: " + state_id_var.get() +
        "\nState: " + state_var.get() +
        "\n\nCity ID: " + city_id_var.get() +
        "\nCity: " + city_var.get()
    )


    messagebox.showinfo(
        "Selected Data",
        message
    )


# ============================================================
# TITLE
# ============================================================

title_label = tk.Label(
    root,
    text="Country - State - City Cascading Dropdown",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=25)


# ============================================================
# FORM FRAME
# ============================================================

form_frame = tk.Frame(root)

form_frame.pack(pady=10)


# ============================================================
# COUNTRY
# ============================================================

tk.Label(
    form_frame,
    text="Country:",
    font=("Arial", 12)
).grid(
    row=0,
    column=0,
    padx=10,
    pady=12,
    sticky="w"
)


country_combo = ttk.Combobox(
    form_frame,
    textvariable=country_var,
    width=30,
    state="readonly"
)

country_combo.grid(
    row=0,
    column=1,
    padx=10,
    pady=12
)


# Load country names

country_names = []

for country in get_countries():

    country_names.append(country["name"])


country_combo["values"] = country_names


# Country select event

country_combo.bind(
    "<<ComboboxSelected>>",
    country_selected
)


# ============================================================
# STATE
# ============================================================

tk.Label(
    form_frame,
    text="State:",
    font=("Arial", 12)
).grid(
    row=1,
    column=0,
    padx=10,
    pady=12,
    sticky="w"
)


state_combo = ttk.Combobox(
    form_frame,
    textvariable=state_var,
    width=30,
    state="readonly"
)

state_combo.grid(
    row=1,
    column=1,
    padx=10,
    pady=12
)


state_combo.bind(
    "<<ComboboxSelected>>",
    state_selected
)


# ============================================================
# CITY
# ============================================================

tk.Label(
    form_frame,
    text="City:",
    font=("Arial", 12)
).grid(
    row=2,
    column=0,
    padx=10,
    pady=12,
    sticky="w"
)


city_combo = ttk.Combobox(
    form_frame,
    textvariable=city_var,
    width=30,
    state="readonly"
)

city_combo.grid(
    row=2,
    column=1,
    padx=10,
    pady=12
)


city_combo.bind(
    "<<ComboboxSelected>>",
    city_selected
)


# ============================================================
# DISPLAY IDS
# ============================================================

id_frame = tk.LabelFrame(
    root,
    text="Selected IDs",
    padx=20,
    pady=10
)

id_frame.pack(
    pady=15
)


tk.Label(
    id_frame,
    text="Country ID:"
).grid(
    row=0,
    column=0,
    padx=10
)

tk.Label(
    id_frame,
    textvariable=country_id_var,
    width=5
).grid(
    row=0,
    column=1
)


tk.Label(
    id_frame,
    text="State ID:"
).grid(
    row=0,
    column=2,
    padx=10
)

tk.Label(
    id_frame,
    textvariable=state_id_var,
    width=5
).grid(
    row=0,
    column=3
)


tk.Label(
    id_frame,
    text="City ID:"
).grid(
    row=0,
    column=4,
    padx=10
)

tk.Label(
    id_frame,
    textvariable=city_id_var,
    width=5
).grid(
    row=0,
    column=5
)


# ============================================================
# BUTTON
# ============================================================

show_button = tk.Button(
    root,
    text="Show Selected Location",
    font=("Arial", 11, "bold"),
    width=25,
    command=show_data
)

show_button.pack(pady=10)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()