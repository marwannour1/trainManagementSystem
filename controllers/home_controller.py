import sys
sys.path.append('C:/Users/Salma/Anaconda/Lib/site-packages') 
import pyodbc as py
import datetime
import sys
from database.connection import conn

class HomeController:
    def __init__(self):
        self.cursor = conn.cursor()

    def get_stations(self):
        self.cursor.execute("SELECT * FROM returnStations()")
        stations_data = self.cursor.fetchall()
        return {row[0]: row[1] for row in stations_data}
        
    def get_station_combo(self,stations):
        # stations=self.get_stations()
        station_combo_values = list(stations.keys())
        return station_combo_values  


    def get_dates(self):
        self.cursor.execute("SELECT Date FROM Tickets")
        dates = [row[0] for row in self.cursor.fetchall()]
        return dates
    
    def done_Atable(self,available_trips_table,stations,start_var,destination_var,date_var):
            #  if date_var.get() != "Date" or stations.get(start_var.get(), 0) !=0 or stations.get(destination_var.get(), 0) !=0 :
            for row in available_trips_table.get_children():
                available_trips_table.delete(row)
            try:
                start_id = stations.get(start_var.get(), 0)
                destination_id = stations.get(destination_var.get(), 0)
                date_id = date_var.get()

                if date_id == "Date":
                    date_id = None

                select = "SELECT * FROM returnATable(?, ?, ?)"
                args = (start_id, destination_id, date_id)

                self.cursor.execute(select, args)
                results = self.cursor.fetchall()

                for row in results:
                    start_station = row[0]
                    destination_station = row[1]
                    trip_date = row[2]

                    available_trips_table.insert(
                        "", "end", values=(start_station, destination_station, trip_date)
                    )
            except Exception as e:
                print(f"Error fetching data: {e}")
 
    def refresh_Atable(self,available_trips_table,stations,start_var,destination_var,date_var):
            start_var.set("Start")
            destination_var.set("Destination")
            date_var.set("Date")

            for row in available_trips_table.get_children():
                available_trips_table.delete(row)
            self.done_Atable(available_trips_table,stations,start_var,destination_var,date_var)

    def done_Ptable(self,previous_trips_table,stations,start_varP,destination_varP,date_varP):
            for row in previous_trips_table.get_children():
                previous_trips_table.delete(row)
            try:
                start_idP = stations.get(start_varP.get(), 0)
                destination_idP = stations.get(destination_varP.get(), 0)
                date_id = date_varP.get()

                if date_id == "Date":
                    date_id = None

                select = "SELECT * FROM returnPTable(?, ?, ?)"
                args = (start_idP, destination_idP, date_id)

                self.cursor.execute(select, args)
                results = self.cursor.fetchall()

                for row in results:
                    start_station = row[0]
                    destination_station = row[1]
                    trip_date = row[2]

                    previous_trips_table.insert(
                        "", "end", values=(start_station, destination_station, trip_date)
                    )

            except Exception as e:
                print(f"Error fetching data: {e}")


    def refresh_Ptable(self,previous_trips_table,stations,start_varP,destination_varP,date_varP):
            start_varP.set("Start")
            destination_varP.set("Destination")
            date_varP.set("Date")

            for row in previous_trips_table.get_children():
                previous_trips_table.delete(row)

            self.done_Ptable(previous_trips_table,stations,start_varP,destination_varP,date_varP)     

    def done_Ctable(self,current_trips_table,stations,start_varC,destination_varC,date_varC):
            #  if date_varC.get() != "Date" or stations.get(start_varC.get(), 0) !=0 or stations.get(destination_varC.get(), 0) !=0 :
            for row in current_trips_table.get_children():
                current_trips_table.delete(row)
            try:
                start_id = stations.get(start_varC.get(), 0)
                destination_id = stations.get(destination_varC.get(), 0)
                date_id = date_varC.get()

                if date_id == "Date":
                    date_id = None

                select = "SELECT * FROM returnCTable(?, ?, ?)"
                args = (start_id, destination_id, date_id)

                self.cursor.execute(select, args)
                results = self.cursor.fetchall()

                for row in results:
                    start_station = row[0]
                    destination_station = row[1]
                    trip_date = row[2]

                    current_trips_table.insert(
                        "", "end", values=(start_station, destination_station, trip_date)
                    )
            except Exception as e:
                print(f"Error fetching data: {e}")


       
    def refresh_Ctable(self,current_trips_table,stations,start_varC,destination_varC,date_varC):
            start_varC.set("Start")
            destination_varC.set("Destination")
            date_varC.set("Date")

            for row in current_trips_table.get_children():
                current_trips_table.delete(row)

            self.done_Ctable(self,current_trips_table,stations,start_varC,destination_varC,date_varC)
    
    
    
    # # To get the selected internal value (station ID) when needed
    # def get_internal_value(combo, named_values):
    #     selected_named_value = combo.get()
    #     return named_values[selected_named_value]