import tkinter as tk
from tkinter import ttk

import pyodbc
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.figure import Figure



def connect_to_db():
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=LAPTOP-49J7V88L;'
                          'DATABASE=TrainManagementSys;'
                          "Trusted_Connection=yes;")
    return conn


# Function to load available seats and trip information for a given train
def load_available_seats_and_trip_info(train_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    # Adjust the query to join Route, Train, and Train_Route tables and fetch additional trip information
    query = """
    SELECT S.Seat_ID, S.price, R.Departure_Time, R.Arrival_Time, R.Station_From, R.Station_To, COUNT(S.Seat_ID) OVER() as TotalSeats
    FROM Seat S
    INNER JOIN Train_Route TR ON S.Train_ID = TR.Train_ID
    INNER JOIN Route R ON TR.Route_ID = R.Route_ID
    WHERE S.Train_ID = ? AND S.Availabilty = 1
    """
    cursor.execute(query, (train_id,))
    seats = cursor.fetchall()
    return [(seat[0], seat[1], seat[2], seat[3], seat[4], seat[5], seat[6]) for seat in seats]

# Function to get the number of available seats for a specific train
# def get_available_seats(train_id):
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     query = """
#     SELECT 
#         (SELECT Seat_Count FROM Train WHERE Train_ID = ?) - 
#         (SELECT COUNT(*) FROM Seat WHERE Train_ID = ? AND Availabilty = 0) AS AvailableSeats
#     """
#     cursor.execute(query, (train_id, train_id))
#     result = cursor.fetchone()
#     return result[0] if result else 0


# def get_total_seats(train_id):
#     conn = connect_to_db()
#     cursor = conn.cursor()
#     query = "SELECT Seat_Count FROM Train WHERE Train_ID = ?"
#     cursor.execute(query, (train_id,))
#     result = cursor.fetchone()
#     return result[0] if result else 0

# GUI setup
root = tk.Tk()
root.title("Train Booking System")

# Assuming you have a way to select a train (not shown here)
# For demonstration, let's assume train_id is obtained from another part of the GUI
train_id = 6 # Example train ID
#available = get_available_seats(train_id)
#total = get_total_seats(train_id)
#total= 100
#available = 50



# Load available seats and trip information for the selected train
available_seats_and_info = load_available_seats_and_trip_info(train_id)

# Create a label to display the selected trip information
selected_trip_info_label = tk.Label(root, text="")
selected_trip_info_label.grid(row=0, column=0, padx=10, pady=10)

# Update the label with the selected trip information
if available_seats_and_info:
    seat_id, price, departure_time, arrival_time, station_from, station_to, total_seats = available_seats_and_info[0]
    selected_trip_info_label.config(text=f"Departure: {departure_time}, Arrival: {arrival_time}, From: {station_from}, To: {station_to}, Seats Available: {total_seats}")


# Create a dropdown menu for selecting a seat
seat_var = tk.StringVar(root)
seat_var.set(available_seats_and_info[0][0]) # Default value
seat_menu = ttk.Combobox(root, textvariable=seat_var, values=[f"{seat[0]} - Price: {seat[1]}" for seat in available_seats_and_info])
seat_menu.grid(row=1, column=0, padx=10, pady=10)

# Book button
def on_book_click():
    seat_id = seat_var.get().split(" - ")[0] # Extract seat ID from the selected option
    print(f"Selected seat ID: {seat_id}")
    # Here, you would proceed with the booking process

book_button = ttk.Button(root, text="Book Seat", command=on_book_click)
book_button.grid(row=2, column=0, padx=10, pady=10)


# Pie chart
#plt.pie([available, total - available], labels=['Available', 'Unavailable'], autopct='%1.1f%%')
#plt.title(f'Seat Availability for Train ID {train_id}')
#plt.show()

root.mainloop()
