import tkinter as tk
from tkinter import ttk

import pyodbc as py
import datetime


conn = py.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-23V77CE;"
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

def done_Atable():
#  if date_var.get() != "Date" or stations.get(start_var.get(), 0) !=0 or stations.get(destination_var.get(), 0) !=0 :
    for row in available_trips_table.get_children():
        available_trips_table.delete(row)
    try:
        start_id = stations.get(start_var.get(), 0)  
        destination_id = stations.get(destination_var.get(), 0)
        date_id=date_var.get()

        
        if date_id == "Date":
                 date_id=None

        
        select = "SELECT * FROM returnATable(?, ?, ?)"
        args = (start_id, destination_id, date_id)

        cursor.execute(select, args)
        results = cursor.fetchall()

        for row in results:
            start_station = row[0]  
            destination_station = row[1]  
            trip_date = row[2]  
    
            available_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
    except Exception as e:
         print(f"Error fetching data: {e}")

# def fill_Atable():
#     try:
#         select = "SELECT * FROM returnAvailable()"
#         cursor.execute(select)
#         results = cursor.fetchall()

#         for row in results:
#             start_station = row[0]  
#             destination_station = row[1]  
#             trip_date = row[2]  

#             available_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
#     except Exception as e:
#          print(f"Error fetching data: {e}")

def refresh_Atable():
    start_var.set("Start")
    destination_var.set("Destination")
    date_var.set("Date")
    
    for row in available_trips_table.get_children():
        available_trips_table.delete(row)

    done_Atable()    

done_Atable()
# Create a "Done" button
done_button = ttk.Button(available_trips_frame, text="Filter", command=done_Atable)
done_button.grid(column=2, row=1, padx=10, pady=5, sticky="w")
refresh_button = ttk.Button(available_trips_frame, text="Reset", command=refresh_Atable)
refresh_button.grid(column=2, row=2, padx=10, pady=5, sticky="w")
book_button = ttk.Button(available_trips_frame, text="Book", command=book_trip)
book_button.grid(column=0, row=2, padx=10, pady=5, sticky="w")


# Frame for previous trips
previous_trips_frame = ttk.LabelFrame(root, text="Previous Trips")
previous_trips_frame.grid(column=1, row=1, padx=10, pady=10, sticky="w")

start_varP = tk.StringVar()
start_varP.set("Start")
destination_varP = tk.StringVar()
destination_varP.set("Destination")
date_varP = tk.StringVar()
date_varP.set("Date")

start_comboP = ttk.Combobox(previous_trips_frame, textvariable=start_varP, state="readonly")
start_comboP.grid(column=0, row=0, padx=5, pady=5, sticky="w")
start_comboP["values"] = start_combo_values

destination_comboP = ttk.Combobox(previous_trips_frame, textvariable=destination_varP, state="readonly")
destination_comboP.grid(column=1, row=0, padx=5, pady=5, sticky="w")
destination_comboP["values"] = destination_combo_values

date_comboP = ttk.Combobox(previous_trips_frame, textvariable=date_varP, state="readonly")
date_comboP.grid(column=2, row=0, padx=5, pady=5, sticky="w")
date_comboP["values"] = dates

# Create a table for previous trips
previous_trips_table = ttk.Treeview(previous_trips_frame, columns=("Start", "Destination", "Date"), show="headings")
previous_trips_table.column("Start", width=100)
previous_trips_table.column("Destination", width=100)
previous_trips_table.column("Date", width=100)
previous_trips_table.heading("Start", text="Start")
previous_trips_table.heading("Destination", text="Destination")
previous_trips_table.heading("Date", text="Date")
previous_trips_table.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w")

def done_Ptable():
#  if date_varP.get() != "Date" or stations.get(start_varP.get(), 0) !=0 or stations.get(destination_varP.get(), 0) !=0 :
    for row in previous_trips_table.get_children():
        previous_trips_table.delete(row)
    try:
        start_idP = stations.get(start_varP.get(), 0)  
        destination_idP = stations.get(destination_varP.get(), 0)
        date_id=date_varP.get()

        
        if date_id == "Date":
                 date_id=None
        
        
        select = "SELECT * FROM returnPTable(?, ?, ?)"
        args = (start_idP, destination_idP, date_id)

        cursor.execute(select, args)
        results = cursor.fetchall()

        for row in results:
            start_station = row[0]  
            destination_station = row[1]  
            trip_date = row[2]  
        
            previous_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
     
    except Exception as e:
         print(f"Error fetching data: {e}")


def refresh_Ptable():
    start_varP.set("Start")
    destination_varP.set("Destination")
    date_varP.set("Date")
    
    for row in previous_trips_table.get_children():
            previous_trips_table.delete(row)
        
    done_Ptable()
    
# def Fill_Ptable():
#     try:
#      select = "SELECT * FROM returnPrevious()"
#      cursor.execute(select)
#      results = cursor.fetchall()

#      for row in results:
#         start_station = row[0]  
#         destination_station = row[1]  
#         trip_date = row[2]  

#         previous_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
#     except Exception as e:
#          print(f"Error fetching data: {e}")

   
done_Ptable()
# Create a "Done" button
done_buttonP = ttk.Button(previous_trips_frame, text="Filter", command=done_Ptable)
done_buttonP.grid(column=2, row=1, padx=10, pady=5, sticky="w")
refresh_buttonP = ttk.Button(previous_trips_frame, text="Reset", command=refresh_Ptable)
refresh_buttonP.grid(column=2, row=2, padx=10, pady=5, sticky="w")



# Frame for current trips
current_trips_frame = ttk.LabelFrame(root, text="current Trips")
current_trips_frame.grid(column=1, row=2, padx=10, pady=10, sticky="w")

start_varC = tk.StringVar()
start_varC.set("Start")
destination_varC = tk.StringVar()
destination_varC.set("Destination")
date_varC = tk.StringVar()
date_varC.set("Date")

start_comboC = ttk.Combobox(current_trips_frame, textvariable=start_varC, state="readonly")
start_comboC.grid(column=0, row=0, padx=5, pady=5, sticky="w")
start_comboC["values"] = start_combo_values

destination_comboC = ttk.Combobox(current_trips_frame, textvariable=destination_varC, state="readonly")
destination_comboC.grid(column=1, row=0, padx=5, pady=5, sticky="w")
destination_comboC["values"] = destination_combo_values

date_comboC = ttk.Combobox(current_trips_frame, textvariable=date_varC, state="readonly")
date_comboC.grid(column=2, row=0, padx=5, pady=5, sticky="w")
date_comboC["values"] = dates



#date_entry = ttk.Entry(current_trips_frame, textvariable=date_varC, width=10)
#date_entry.grid(column=2, row=0, padx=5, pady=5, sticky="w")

# Create a table for current trips
current_trips_table = ttk.Treeview(current_trips_frame, columns=("Start", "Destination", "Date"), show="headings")
current_trips_table.column("Start", width=100)
current_trips_table.column("Destination", width=100)
current_trips_table.column("Date", width=100)
current_trips_table.heading("Start", text="Start")
current_trips_table.heading("Destination", text="Destination")
current_trips_table.heading("Date", text="Date")
current_trips_table.grid(column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w")

# Add sample data to the current trips table
# for row in cursor.fetchall():
#     current_trips_table.insert("", "end", values=row)

def done_Ctable():
#  if date_varC.get() != "Date" or stations.get(start_varC.get(), 0) !=0 or stations.get(destination_varC.get(), 0) !=0 :
    for row in current_trips_table.get_children():
        current_trips_table.delete(row)
    try:
        start_id = stations.get(start_varC.get(), 0)  
        destination_id = stations.get(destination_varC.get(), 0)
        date_id=date_varC.get()

        
        if date_id == "Date":
                 date_id=None

        
        select = "SELECT * FROM returnCTable(?, ?, ?)"
        args = (start_id, destination_id, date_id)

        cursor.execute(select, args)
        results = cursor.fetchall()

        for row in results:
            start_station = row[0]  
            destination_station = row[1]  
            trip_date = row[2]  
    
            current_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
    except Exception as e:
         print(f"Error fetching data: {e}")

# def fill_Ctable():
#     try:
#         select = "SELECT * FROM returnCurrent()"
#         cursor.execute(select)
#         results = cursor.fetchall()

#         for row in results:
#             start_station = row[0]  
#             destination_station = row[1]  
#             trip_date = row[2]  

#             current_trips_table.insert("", "end", values=(start_station, destination_station, trip_date))
#     except Exception as e:
#          print(f"Error fetching data: {e}")

def refresh_Ctable():
    start_varC.set("Start")
    destination_varC.set("Destination")
    date_varC.set("Date")
    
    for row in current_trips_table.get_children():
        current_trips_table.delete(row)

    done_Ctable()    

done_Ctable()
# Create a "Done" button
done_buttonC = ttk.Button(current_trips_frame, text="Filter", command=done_Ctable)
done_buttonC.grid(column=2, row=1, padx=10, pady=5, sticky="w")
refresh_buttonC = ttk.Button(current_trips_frame, text="Reset", command=refresh_Ctable)
refresh_buttonC.grid(column=2, row=2, padx=10, pady=5, sticky="w")
cancel_button = ttk.Button(current_trips_frame, text="Cancel", command=cancel_trip)
cancel_button.grid(column=0, row=2, padx=10, pady=10, sticky="w")



root.mainloop()