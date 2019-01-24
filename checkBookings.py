# imports pandas module
import pandas as pd

import time

# 
start = time.time()

# creates pandas dataframe from room booking data (useful for very lareg datasets)
room_data = pd.read_csv("data/room_booking_data.csv")

# checkBookings function
# determines if any bookings made conflict with one another

def checkBookings(room_data):

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


# invokes the checkBookings function
checkBookings(room_data)


end = time.time()
print(end - start)
