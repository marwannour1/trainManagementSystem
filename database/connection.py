"""This module contains the implementation of the database connection."""

import pyodbc as py

conn = py.connect(
    "Driver={SQL Server};"
    "Server=NEBULA;"
    "Database=TrainManagementSys;"
    "Trusted_Connection=yes;"
)
