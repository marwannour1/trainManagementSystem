"""This module contains the implementation of the database connection."""

import sys

sys.path.append("C:/Users/Salma/Anaconda/Lib/site-packages")
import pyodbc as py

conn = py.connect(
    "Driver={SQL Server};"
    "Server=NEBULA;"
    "Database=TrainManagementSys;"
    "Trusted_Connection=yes;"
)


import pyodbc


def connect_to_db():
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "Server=NEBULA;"
        "DATABASE=TrainManagementSys;"
        "Trusted_Connection=yes;"
    )
    return conn


def load_available_seats_and_trip_info(train_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = """
    SELECT S.Seat_ID, S.price, R.Departure_Time, R.Arrival_Time, R.Station_From, R.Station_To, COUNT(S.Seat_ID) OVER() as TotalSeats
    FROM Seat S
    INNER JOIN Train_Route TR ON S.Train_ID = TR.Train_ID
    INNER JOIN Route R ON TR.Route_ID = R.Route_ID
    WHERE S.Train_ID = ?
    """
    cursor.execute(query, (train_id,))
    seats = cursor.fetchall()
    return [
        (seat[0], seat[1], seat[2], seat[3], seat[4], seat[5], seat[6])
        for seat in seats
    ]
