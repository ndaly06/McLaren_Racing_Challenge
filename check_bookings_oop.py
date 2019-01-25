# imports the python pandas module
import pandas as pd

# CheckBookings parent class
class CheckBookings:

    #  constructor
    def __init__(self, filepath):
        self.filepath = filepath

    def read_file(self):

        try:
            # reads in the csv and creates pandas dataframe
            booking_data = pd.read_csv(self.filepath)
            return booking_data

        # my_file_handle = open(filepath)
        except IOError:
            print("File not found or path is incorrect")
        

    def check_bookings(self):

        try:
            # reads in the csv and creates pandas dataframe
            room_data = pd.read_csv(self.filepath)
            # return booking_data

        # my_file_handle = open(filepath)
        except IOError:
            print("File not found or path is incorrect")

        # room_data = CheckBookings.read_file(self)

        # print(booking_data)

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


#
test1 = CheckBookings("data/room_booking_data.csv")

test2 = CheckBookings("data/room_booking_da.csv")

#
test1.check_bookings()