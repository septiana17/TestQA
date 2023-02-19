from datetime import datetime
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

# Create a cursor object
cursor = db.cursor()

# Retrieve all bookings for the given date and time range
date = "2022-12-10"
start_time = "09:00:00"
end_time = "11:00:00"
query = "SELECT * FROM booking WHERE date = %s AND ((start_time <= %s AND end_time > %s) OR (start_time >= %s AND start_time < %s))"
values = (date, start_time, start_time, start_time, end_time)
cursor.execute(query, values)
bookings = cursor.fetchall()

# Check if there is a double booking
if len(bookings) > 1:
    print("Double booking detected!")

# Retrieve the correct price for the given date and time range
query = "SELECT price FROM schedule WHERE venue_id = %s AND date = %s AND start_time = %s AND end_time = %s"
values = (15, date, start_time, end_time)
cursor.execute(query, values)
price = cursor.fetchone()[0]

# Retrieve the price for each booking
booking_prices = [booking[6] for booking in bookings]

# Check if the prices match
if price not in booking_prices:
    print("Incorrect price detected!")
    
# Close the database connection
db.close()
