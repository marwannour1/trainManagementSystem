"""This module contains the implementation of the database connection."""

import pyodbc as py

conn = py.connect(
    "Driver={SQL Server};"
    "Server=DESKTOP-23V77CE;"
    "Database=TrainManagementSys;"
    "Trusted_Connection=yes;"
)


import pyodbc


def connect_to_db():
    conn = pyodbc.connect(
        "DRIVER={SQL Server};"
        "SERVER=NEBULA;"
        "DATABASE=TrainManagementSys;"
        "Trusted_Connection=yes;"
    )
    return conn
