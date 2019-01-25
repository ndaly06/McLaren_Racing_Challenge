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


        # 
        def read_file(self):
            
            # try statement
            try:

                # if the file size is greater than zero
                if os.path.getsize(self.filepath) > 0:

                    # reads in the csv and creates pandas dataframe
                    room_data = pd.read_csv(self.filepath)

                    return room_data

                else:
                    # 
                    return "File is empty or no arguments passed"

            except IOError:
            
                return ("File not found or path is incorrect")

        
        #
        room_data = self.read_file()

        return room_data

        # # boolean flag (tentatively set as false)
        # conflicts_present = False

        # # for loop
        # for i in range(len(room_data) - 1):

        #     # nested for loop
        #     for j in range(i + 1, len(room_data)):

        #         """

        #         first booking start time = 9am
        #         first booking end time = 11am                    
                
        #         second booking start time = 10am
        #         second booking end time = 1pm

        #         if the first booking start time is less than the second booking end time and if
        #         the first booking end time is greater than the second booking start time a conflict has occurred
        #         as the second booking cannot exist between the first booking time range

        #         """
        #         if (room_data['Start_Time'].iloc[i] < room_data['End_Time'].iloc[j]) and (room_data['End_Time'].iloc[i] > room_data['Start_Time'].iloc[j]):

        #             # sets the conflicts boolean flag to true (as conflicts have been detected)
        #             conflicts_present = True


        #             return ("Conflict between request",
        #                             room_data["Request_ID"].iloc[i], "and request", room_data["Request_ID"].iloc[j])

        #             # return ("Conflict between request",
        #             #         room_data["Request_ID"].iloc[i], "and request", room_data["Request_ID"].iloc[j])

        #             # return conflicts

        #             # print("Conflict between request",
        #             #         room_data["Request_ID"].iloc[i], "and request", room_data["Request_ID"].iloc[j])

        #     # if the conflicts flag is False
        #     if not conflicts_present:
        #         #
        #         return "No booking conflicts identified"


#
filepath = "testda.csv"

#
print(CheckBookings(filepath))
