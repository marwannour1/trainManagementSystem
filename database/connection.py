"""This module contains the implementation of the database connection."""
import sys
sys.path.append('C:/Users/Salma/Anaconda/Lib/site-packages') 

import pyodbc as py

conn = py.connect(
    "Driver={SQL Server};"
     "Server=MSI;"
    "Database=TrainManagementSys;"
    "Trusted_Connection=yes;"
)
