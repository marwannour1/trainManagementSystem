import tkinter as tk
from tkinter import ttk
from database import load_available_seats_and_trip_info


class TrainBookingGUI:
    def __init__(self, root):
        self.root = root
        self.train_id = 6  # Example train ID
        self.available_seats_and_info = load_available_seats_and_trip_info(
            self.train_id
        )
        self.gui_frame = self.setup_gui()
        self.gui_frame.pack(padx=10, pady=10)

    def setup_gui(self):
        gui_frame = tk.Frame(self.root)

        selected_trip_info_label = tk.Label(gui_frame, text="")
        selected_trip_info_label.grid(row=0, column=0, padx=10, pady=10)

        if self.available_seats_and_info:
            (
                seat_id,
                price,
                departure_time,
                arrival_time,
                station_from,
                station_to,
                total_seats,
            ) = self.available_seats_and_info[0]
            selected_trip_info_label.config(
                text=f"Departure: {departure_time}, Arrival: {arrival_time}, From: {station_from}, To: {station_to}, Seats Available: {total_seats}"
            )

        seat_var = tk.StringVar(gui_frame)
        seat_var.set(self.available_seats_and_info[0][0])  # Default value
        seat_menu = ttk.Combobox(
            gui_frame,
            textvariable=seat_var,
            values=[
                f"{seat[0]} - Price: {seat[1]}"
                for seat in self.available_seats_and_info
            ],
        )
        seat_menu.grid(row=1, column=0, padx=10, pady=10)

        book_button = ttk.Button(gui_frame, text="Book Seat", command=on_book_click)
        book_button.grid(row=2, column=0, padx=10, pady=10)

        return gui_frame


def main():
    root = tk.Tk()
    root.title("Train Booking System")
    TrainBookingGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
