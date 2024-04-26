import tkinter as tk
from tkinter import ttk


def book_trip():
    pass


def cancel_trip():
    pass


from controllers.home_controller import HomeController
from controllers.login_controller import LoginController


class HomePage:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.selected_items = []
        self.create_main_page()

    def create_main_page(self):

        header_label = ttk.Label(
            self.root,
            text=f"Welcome, {LoginController.loginID}!",
            font=("Arial", 16, "bold"),
        )
        header_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

        # Frame for available trips
        available_trips_frame = ttk.LabelFrame(self.root, text="Available Trips")
        available_trips_frame.grid(column=0, row=1, padx=10, pady=10, sticky="w")

        start_var = tk.StringVar()
        start_var.set("Start")
        destination_var = tk.StringVar()
        destination_var.set("Destination")
        date_var = tk.StringVar()
        date_var.set("Date")
        stations = self.controller.get_stations()

        start_combo = ttk.Combobox(
            available_trips_frame, textvariable=start_var, state="readonly"
        )
        start_combo.grid(column=0, row=0, padx=5, pady=5, sticky="w")
        start_combo["values"] = self.controller.get_station_combo(stations)

        destination_combo = ttk.Combobox(
            available_trips_frame, textvariable=destination_var, state="readonly"
        )
        destination_combo.grid(column=1, row=0, padx=5, pady=5, sticky="w")
        destination_combo["values"] = self.controller.get_station_combo(stations)


        available_trips_table = ttk.Treeview(
            available_trips_frame,
            columns=("Start", "Destination", "Arrival Time","Departure Time"),
            show="headings",
        )
        available_trips_table.column("Start", width=100)
        available_trips_table.column("Destination", width=100)
        available_trips_table.column("Departure Time", width=100)
        available_trips_table.column("Arrival Time", width=100)
        available_trips_table.heading("Start", text="Start")
        available_trips_table.heading("Destination", text="Destination")
        available_trips_table.heading("Departure Time", text="Departure_Time")
        available_trips_table.heading("Arrival Time", text="Arrival_Time")

        available_trips_table.grid(
            column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w"
        )

        self.controller.done_Atable(
            available_trips_table, stations, start_var, destination_var
        )

        done_button = ttk.Button(
            available_trips_frame,
            text="Filter",
            command=lambda: self.done_Atable(
                available_trips_table, stations, start_var, destination_var
            ),
        )
        done_button.grid(column=1, row=2, padx=10, pady=5, sticky="w")

        refresh_button = ttk.Button(
            available_trips_frame,
            text="Reset",
            command=lambda: self.refresh_Abutton(
                available_trips_table, stations, start_var, destination_var
            ),
        )
        refresh_button.grid(column=2, row=2, padx=10, pady=5, sticky="w")
        refresh_button = ttk.Button(
            available_trips_frame,
            text="Reset",
            command=lambda: self.refresh_Atable(
                previous_trips_table, stations, start_varP, destination_varP
            ),
        )
        
        # selected_item = None
        def handle_row_selection(event):
            selected_item = available_trips_table.selection()
            if selected_item:

                print("Selected item:", selected_item)
                self.selected_items = available_trips_table.item(selected_item, 'values')
                # selected_values(item_values)
                return selected_item
            else:
                print("No item selected")
                return None
            
        # # def selected_values(item):
        # #         selected_item= item
        # #         return selected_item

        available_trips_table.bind('<<TreeviewSelect>>', handle_row_selection)

        # def routeID():
        #     global selected_item  # Access the selected item from the global variable
        #     if selected_item:
        #         route_id = selected_item  # Assuming the route ID is stored in the first column
        #         return route_id
        #     else:
        #         print("No item selected")
        #         return None
            
        # item=routeID()



        # selected_item=selected_values
        # if selected_item:
        #         start = selected_item[0]  # Assuming start is the first column
        #         destination = selected_item[1]  # Assuming destination is the second column
        #         arrival_time = selected_item[2]  # Assuming arrival time is the third column
        #         departure_time = selected_item[3] 
        #         print(start, destination, arrival_time, departure_time)
        # else:
        #         # Handle case when no item is selected
        #         print("No item selected")        


        # def on_row_select(self, event):
        #     selected_item = self.available_trips_table.focus()
        #     item_details = self.available_trips_table.item(selected_item)
        #     self.selected_items = item_details['values']

        book_button = ttk.Button(available_trips_frame, text="Book", command=lambda: self.get_routeID(self.selected_items,available_trips_table, stations))
        book_button.grid(column=0, row=2, padx=10, pady=5, sticky="w")

        # Frame for previous trips
        previous_trips_frame = ttk.LabelFrame(self.root, text="Previous Trips")
        previous_trips_frame.grid(column=1, row=1, padx=10, pady=10, sticky="w")

        start_varP = tk.StringVar()
        start_varP.set("Start")
        destination_varP = tk.StringVar()
        destination_varP.set("Destination")
        date_varP = tk.StringVar()
        date_varP.set("Date")

        start_comboP = ttk.Combobox(
            previous_trips_frame, textvariable=start_varP, state="readonly"
        )
        start_comboP.grid(column=0, row=0, padx=5, pady=5, sticky="w")
        start_comboP["values"] = self.controller.get_station_combo(stations)

        destination_comboP = ttk.Combobox(
            previous_trips_frame, textvariable=destination_varP, state="readonly"
        )
        destination_comboP.grid(column=1, row=0, padx=5, pady=5, sticky="w")
        destination_comboP["values"] = self.controller.get_station_combo(stations)

        date_comboP = ttk.Combobox(
            previous_trips_frame, textvariable=date_varP, state="readonly"
        )
        date_comboP.grid(column=2, row=0, padx=5, pady=5, sticky="w")
        date_comboP["values"] = self.controller.get_dates()

        # Create a table for previous trips
        previous_trips_table = ttk.Treeview(
            previous_trips_frame,
            columns=("Start", "Destination", "Date"),
            show="headings",
        )
        previous_trips_table.column("Start", width=100)
        previous_trips_table.column("Destination", width=100)
        previous_trips_table.column("Date", width=100)
        previous_trips_table.heading("Start", text="Start")
        previous_trips_table.heading("Destination", text="Destination")
        previous_trips_table.heading("Date", text="Date")
        previous_trips_table.grid(
            column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w"
        )

        self.controller.done_Ptable(
            previous_trips_table, stations, start_varP, destination_varP, date_varP
        )

        done_buttonP = ttk.Button(
            previous_trips_frame,
            text="Filter",
            command=lambda: self.done_Ptable(
                previous_trips_table, stations, start_varP, destination_varP, date_varP
            ),
        )
        done_buttonP.grid(column=1, row=2, padx=10, pady=5, sticky="w")
        refresh_buttonP = ttk.Button(
            previous_trips_frame,
            text="Reset",
            command=lambda: self.refresh_Pbutton(
                previous_trips_table, stations, start_varP, destination_varP, date_varP
            ),
        )
        refresh_buttonP.grid(column=2, row=2, padx=10, pady=5, sticky="w")

        # Frame for current trips
        current_trips_frame = ttk.LabelFrame(self.root, text="current Trips")
        current_trips_frame.grid(column=1, row=2, padx=10, pady=10, sticky="w")

        start_varC = tk.StringVar()
        start_varC.set("Start")
        destination_varC = tk.StringVar()
        destination_varC.set("Destination")
        date_varC = tk.StringVar()
        date_varC.set("Date")

        start_comboC = ttk.Combobox(
            current_trips_frame, textvariable=start_varC, state="readonly"
        )
        start_comboC.grid(column=0, row=0, padx=5, pady=5, sticky="w")
        start_comboC["values"] = self.controller.get_station_combo(stations)

        destination_comboC = ttk.Combobox(
            current_trips_frame, textvariable=destination_varC, state="readonly"
        )
        destination_comboC.grid(column=1, row=0, padx=5, pady=5, sticky="w")
        destination_comboC["values"] = self.controller.get_station_combo(stations)

        date_comboC = ttk.Combobox(
            current_trips_frame, textvariable=date_varC, state="readonly"
        )
        date_comboC.grid(column=2, row=0, padx=5, pady=5, sticky="w")
        date_comboC["values"] = self.controller.get_dates()

        current_trips_table = ttk.Treeview(
            current_trips_frame,
            columns=("Start", "Destination", "Date"),
            show="headings",
        )
        current_trips_table.column("Start", width=100)
        current_trips_table.column("Destination", width=100)
        current_trips_table.column("Date", width=100)
        current_trips_table.heading("Start", text="Start")
        current_trips_table.heading("Destination", text="Destination")
        current_trips_table.heading("Date", text="Date")
        current_trips_table.grid(
            column=0, row=1, columnspan=3, padx=5, pady=5, sticky="w"
        )

        self.controller.done_Ctable(
            current_trips_table, stations, start_varC, destination_varC, date_varC
        )

        done_buttonC = ttk.Button(
            current_trips_frame,
            text="Filter",
            command=lambda: self.done_Ctable(
                current_trips_table, stations, start_varC, destination_varC, date_varC
            ),
        )
        done_buttonC.grid(column=1, row=2, padx=10, pady=5, sticky="w")
        refresh_buttonC = ttk.Button(
            current_trips_frame,
            text="Reset",
            command=lambda: self.refresh_Cbutton(
                current_trips_table, stations, start_varC, destination_varC, date_varC
            ),
        )
        refresh_buttonC.grid(column=2, row=2, padx=10, pady=5, sticky="w")
        cancel_button = ttk.Button(
            current_trips_frame, text="Cancel", command=cancel_trip
        )
        cancel_button.grid(column=0, row=2, padx=10, pady=10, sticky="w")

    def refresh_Pbutton(
        self, previous_trips_table, stations, start_varP, destination_varP, date_varP
    ):
        self.controller.refresh_Ptable(
            previous_trips_table, stations, start_varP, destination_varP, date_varP
        )

    def refresh_Abutton(
        self, available_trips_table, stations, start_var, destination_var
    ):
        self.controller.refresh_Atable(
            available_trips_table, stations, start_var, destination_var
        )

    def refresh_Cbutton(
        self, current_trips_table, stations, start_varC, destination_varC, date_varC
    ):
        self.controller.refresh_Ctable(
            current_trips_table, stations, start_varC, destination_varC, date_varC
        )

    def done_Atable(
        self, available_trips_table, stations, start_var, destination_var
    ):
        self.controller.done_Atable(
            available_trips_table, stations, start_var, destination_var
        )

    def done_Ptable(
        self, previous_trips_table, stations, start_varP, destination_varP, date_varP
    ):
        self.controller.done_Ptable(
            previous_trips_table, stations, start_varP, destination_varP, date_varP
        )

    def done_Ctable(
        self, current_trips_table, stations, start_varC, destination_varC, date_varC
    ):
        self.controller.done_Ctable(
            current_trips_table, stations, start_varC, destination_varC, date_varC
        )
    def get_routeID(self,selected_item,available_trips_table, stations):
        self.controller.get_routeID(selected_item,available_trips_table, stations)
