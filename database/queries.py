import pyodbc as py
from database.connection import conn


def get_stations():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM returnStations()")
    stations_data = cursor.fetchall()
    return {row[0]: row[1] for row in stations_data}


def get_dates():
    cursor = conn.cursor()
    cursor.execute("SELECT Date FROM Tickets")
    dates = [row[0] for row in cursor.fetchall()]
    return dates


def get_trips(start_id, destination_id, date_id):
    cursor = conn.cursor()
    select = "SELECT * FROM returnATable(?, ?, ?)"
    args = (start_id, destination_id, date_id)
    cursor.execute(select, args)
    return cursor.fetchall()


# Add similar functions for previous and current trips as needed
