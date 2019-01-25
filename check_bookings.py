# imports pandas module
import pandas as pd
import time

#
""" 
    This is a class that detects room booking conflicts. 
      
    Attributes: 
        real (int): The real part of complex number. 
        imag (int): The imaginary part of complex number. 
    """


class CheckBookings():

    # "data/room_booking_data.csv"

    # readData function


def read_data(filepath):

    # creates pandas dataframe from room booking data (useful for very lareg datasets)
    room_data = pd.read_csv(filepath)

    return room_data
# end of readData function


# start = time.time()

# checkBookings function
# determines if any bookings made conflict with one another
def check_bookings(room_data):

    # boolean flag (tentatively set as false)
    conflicts = False

    # for loop
    for i in range(len(room_data) - 1):

        # nested for loop
        for j in range(i + 1, len(room_data)):

            #
            if (room_data['Start_Time'].iloc[i] < room_data['End_Time'].iloc[j]) and (room_data['End_Time'].iloc[i] > room_data['Start_Time'].iloc[j]):

                # sets the conflicts boolean flag to true (as conflicts have been detected)
                conflicts = True

                print("Conflict between booking",
                      room_data["Booking_ID"].iloc[i], "and booking", room_data["Booking_ID"].iloc[j])

    # if the conflicts flag is False
    if not conflicts:
        print("No booking conflicts identified")
# end of checkBookings function

#####################################

#
filepath = "data/room_booking_data.csv"

#
data = readData(filepath)

print(data)

# invokes the checkBookings function
# checkBookings(room_data)


# end = time.time()
# print(end - start)
