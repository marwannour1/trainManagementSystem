import tkinter as tk
from tkinter import ttk
import sys 
sys.path.append('C:/Users/Salma/Anaconda/Lib/site-packages') 
import pyodbc as py

conn = py.connect(
    "Driver={SQL Server};"
    "Server=MSI;"
    "Database=TrainManagementSys;"
    "Trusted_Connection=yes;"
)

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM Route")
cursor = conn.cursor()

# Station = conn.cursor()
# Station.execute("SELECT * FROM Station")

# for i in cursor:
#     print(i)

def book_trip():
    # Implement booking logic here
    pass

def cancel_trip():
    # Implement cancel logic here
    pass

# Fetch distinct date values from the Tickets table
cursor.execute("SELECT Date FROM Tickets")
dates = [row[0] for row in cursor.fetchall()]  # Assuming the first column is the Date




root = tk.Tk()

# Fetch stations data from the returnStations function
cursor.execute("SELECT * FROM returnStations()")
stations_data = cursor.fetchall()

# Create stations dictionary from fetched data
stations = {row[0]: row[1] for row in stations_data}

# Populate start_combo with named values
start_combo_values = list(stations.keys())

# Populate destination_combo with named values
destination_combo_values = list(stations.keys())


# To get the selected internal value (station ID) when needed
def get_internal_value(combo, named_values):
    selected_named_value = combo.get()
    return named_values[selected_named_value]

# Create a header
header_label = ttk.Label(root, text="Welcome, User!", font=("Arial", 16, "bold"))
header_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

# Frame for available trips
available_trips_frame = ttk.LabelFrame(root, text="Available Trips")
available_trips_frame.grid(column=0, row=1, padx=10, pady=10, sticky="w")

start_var = tk.StringVar()
start_var.set("Start")
destination_var = tk.StringVar()
destination_var.set("Destination")
date_var = tk.StringVar()
date_var.set("Date")

start_combo = ttk.Combobox(available_trips_frame, textvariable=start_var, state="readonly")
start_combo.grid(column=0, row=0, padx=5, pady=5, sticky="w")
start_combo["values"] = start_combo_values

destination_combo = ttk.Combobox(available_trips_frame, textvariable=destination_var, state="readonly")
destination_combo.grid(column=1, row=0, padx=5, pady=5, sticky="w")
destination_combo["values"] = destination_combo_values

date_combo = ttk.Combobox(available_trips_frame, textvariable=date_var, state="readonly")
date_combo.grid(column=2, row=0, padx=5, pady=5, sticky="w")
# Populate date_combo with fetched date values
date_combo["values"] = dates



#date_entry = ttk.Entry(available_trips_frame, textvariable=date_var, width=10)
#date_entry.grid(column=2, row=0, padx=5, pady=5, sticky="w")

# Create a table for available trips
available_trips_table = ttk.Treeview(available_trips_frame, columns=("Start", "Destination", "Date"), show="headings")
available_trips_table.column("Start", width=100)
available_trips_table.column("Destination", width=100)
available_trips_table.column("Date", width=100)
available_trips_table.heading("Start", text="Start")
available_trips_table.heading("Destination", text="Destination")
available_trips_table.heading("Date", text="Date")
available_trips_table.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w")

# Add sample data to the available trips table
# for row in cursor.fetchall():
#     available_trips_table.insert("", "end", values=row)

def refresh_table():
# if date_var.get() != "Date":
    for row in available_trips_table.get_children():
        available_trips_table.delete(row)
    try:
        start_id = stations.get(start_var.get(), 0)  
        destination_id = stations.get(destination_var.get(), 0)

        # date_value = date_var.get()
        # if date_value == "Date":
        #     date_value = 0

        
        select = "SELECT * FROM returnTable(?, ?, ?)"
        args = (start_id, destination_id, date_var.get())

        cursor.execute(select, args)
        results = cursor.fetchall()

        for row in results:
            start_station = row[0]  
            destination_station = row[1]  
            trip_date = row[2]  
    
            available_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
    except Exception as e:
         print(f"Error fetching data: {e}")



# Create a "Done" button
done_button = ttk.Button(available_trips_frame, text="Done", command=refresh_table)
done_button.grid(column=2, row=1, padx=10, pady=5, sticky="w")
try:
    select = "SELECT * FROM returnAvailable()"
    cursor.execute(select)
    results = cursor.fetchall()

    for row in results:
        start_station = row[0]  
        destination_station = row[1]  
        trip_date = row[2]  

        available_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
except Exception as e:
         print(f"Error fetching data: {e}")


# Frame for previous trips
previous_trips_frame = ttk.LabelFrame(root, text="Previous Trips")
previous_trips_frame.grid(column=1, row=1, padx=10, pady=10, sticky="w")

start_combo = ttk.Combobox(previous_trips_frame, textvariable=start_var, state="readonly")
start_combo.grid(column=0, row=0, padx=5, pady=5, sticky="w")

destination_combo = ttk.Combobox(previous_trips_frame, textvariable=destination_var, state="readonly")
destination_combo.grid(column=1, row=0, padx=5, pady=5, sticky="w")

date_combo = ttk.Combobox(previous_trips_frame, textvariable=date_var, state="readonly")
date_combo.grid(column=2, row=0, padx=5, pady=5, sticky="w")

# Create a table for previous trips
previous_trips_table = ttk.Treeview(previous_trips_frame, columns=("Start", "Destination", "Date"), show="headings")
previous_trips_table.column("Start", width=100)
previous_trips_table.column("Destination", width=100)
previous_trips_table.column("Date", width=100)
previous_trips_table.heading("Start", text="Start")
previous_trips_table.heading("Destination", text="Destination")
previous_trips_table.heading("Date", text="Date")
previous_trips_table.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w")

# Add sample data to the previous trips table
for i in range(4):
    previous_trips_table.insert("", "end", values=("Start " + str(i), "Destination " + str(i), "Date " + str(i)))

# Frame for currently booked trips
currently_booked_trips_frame = ttk.LabelFrame(root, text="Currently Booked Trips")
currently_booked_trips_frame.grid(column=1, row=2, padx=10, pady=10, sticky="w")

start_combo = ttk.Combobox(currently_booked_trips_frame, textvariable=start_var, state="readonly")
start_combo.grid(column=0, row=0, padx=5, pady=5, sticky="w")

destination_combo = ttk.Combobox(currently_booked_trips_frame, textvariable=destination_var, state="readonly")
destination_combo.grid(column=1, row=0, padx=5, pady=5, sticky="w")

date_combo = ttk.Combobox(currently_booked_trips_frame, textvariable=date_var, state="readonly")
date_combo.grid(column=2, row=0, padx=5, pady=5, sticky="w")

# Create a table for currently booked trips
currently_booked_trips_table = ttk.Treeview(currently_booked_trips_frame, columns=("Start", "Destination", "Date"), show="headings")
currently_booked_trips_table.column("Start", width=100)
currently_booked_trips_table.column("Destination", width=100)
currently_booked_trips_table.column("Date", width=100)
currently_booked_trips_table.heading("Start", text="Start")
currently_booked_trips_table.heading("Destination", text="Destination")
currently_booked_trips_table.heading("Date", text="Date")
currently_booked_trips_table.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w")

# Add sample data to the currently booked trips table
for i in range(3):
    currently_booked_trips_table.insert("", "end", values=("Start " + str(i), "Destination " + str(i), "Date " + str(i)))


# Buttons
book_button = ttk.Button(root, text="Book", command=book_trip)
book_button.grid(column=0, row=4, padx=10, pady=10, sticky="w")

cancel_button = ttk.Button(root, text="Cancel", command=cancel_trip)
cancel_button.grid(column=1, row=4, padx=10, pady=10, sticky="w")

root.mainloop()