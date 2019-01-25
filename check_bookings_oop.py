# imports the python pandas module
import pandas as pd
import os

# CheckBookings parent class
class CheckBookings:

    #  constructor
    def __init__(self, filepath):
        self.filepath = filepath
        
    # check_bookings method
    def check_bookings(self):

        # try statement
        try:

# "data/room_booking_data.csv"
            if os.path.getsize(self.filepath) > 0:

                # reads in the csv and creates pandas dataframe
                room_data = pd.read_csv(self.filepath)

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

            else: 
                print("File is empty or no arguments passed")

        # my_file_handle = open(filepath)
        except IOError:
            print("File not found or path is incorrect")

        # except TypeError:
        #     print("ppo")

    # end of checkBookings method

    # room_data = CheckBookings.read_file(self)

    # or len(self.filepath) > 0


        
# TESTS

# empty csv passed
test1 = CheckBookings("data/testdata1.csv")

# csv containing no conflicts passed
test2 = CheckBookings("data/testdata2.csv")

# csv containing conflicts passed
test3 = CheckBookings("data/testdata3.csv")

# incorrect path provided
test4 = CheckBookings("data/room_booking.csv")



#
test3.check_bookings()
