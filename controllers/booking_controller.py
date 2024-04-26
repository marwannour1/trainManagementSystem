import pyodbc
from database.connection import conn


class BookingController:

    @staticmethod
    def load_available_seats_and_trip_info(train_id):
        query = """
        SELECT S.Seat_ID, S.price, R.Departure_Time, R.Arrival_Time, R.Station_From, R.Station_To, COUNT(S.Seat_ID) OVER() as TotalSeats
        FROM Seat S
        INNER JOIN Train_Route TR ON S.Train_ID = TR.Train_ID
        INNER JOIN Route R ON TR.Route_ID = R.Route_ID
        WHERE S.Train_ID = ?;
        """
        cursor = conn.cursor()
        cursor.execute(query, (train_id,))
        seats = cursor.fetchall()
        return [
            (seat[0], seat[1], seat[2], seat[3], seat[4], seat[5], seat[6])
            for seat in seats
        ]

    @staticmethod
    def book_seat(seat_id):
        # Implement the logic to book a seat here
        print(f"Seat {seat_id} booked.")
        return True
