# imports the python pandas module
import pandas as pd
import os

# CheckBookings parent class

""" CheckBookings parent class """


class CheckBookings:

    #  constructor
    def __init__(self, filepath):
        self.filepath = filepath

    # check_bookings method
    def check_bookings(self):
        
        try:
            # f = open(fname, 'rb')
            # reads in the csv and creates pandas dataframe
            room_data = pd.read_csv(self.filepath)

            # 
            conflicts = []

            # 
            for i in range(len(room_data)):

                # nested for loop
                for j in range(i + 1, len(room_data)):

                    if (room_data['Start_Time'].iloc[i] < room_data['End_Time'].iloc[j]) and (room_data['End_Time'].iloc[i] > room_data['Start_Time'].iloc[j]):

                        conflicts.append(("Conflict between request",
                                    room_data["Request_ID"].iloc[i], "and request", room_data["Request_ID"].iloc[j]))


            return conflicts


            
        
        except IOError:
            return "Could not read file:", filepath
        # sys.exit()


#
filepath = "data/testdata6.csv"

print(CheckBookings(filepath).check_bookings())

# with f:
#     reader = csv.reader(f)
#     for row in reader:
#         pass #do stuff here