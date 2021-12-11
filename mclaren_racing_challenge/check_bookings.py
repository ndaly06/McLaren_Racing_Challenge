import os
import sys

import pandas as pd


class CheckBookings:
    """
    CheckBookings class: determines if any of the booking requests
    in a file conflict with each other.

    Attributes:
        filepath: path to the file that contains the room booking data to be
        checked for potential booking conflicts.
    """

    def __init__(self, filepath):
        """constructor initialises the CheckBookings class"""
        self.filepath = filepath

    def check_bookings(self):
        """
        check_bookings class method that checks the bookings made to identify
        if any conflict with each other.
        """
        try:
            # If the file size is greater than zero (not empty).
            if os.path.getsize(self.filepath) > 0:
                room_data = pd.read_csv(self.filepath)
                conflicts = []
                # Conflicts_present boolean flag set tentitively as False.
                conflicts_present = False

                for i in range(len(room_data)):
                    for j in range(i + 1, len(room_data)):
                        if (
                            room_data["Start_Time"].iloc[i]
                            < room_data["End_Time"].iloc[j]
                            and room_data["End_Time"].iloc[i]
                            > room_data["Start_Time"].iloc[j]
                        ):
                            # Conflicts detected so flag set as True.
                            conflicts_present = True
                            conflicts.append(
                                (
                                    "Booking conflict detected between request",
                                    room_data["Request_ID"].iloc[i],
                                    "and request",
                                    room_data["Request_ID"].iloc[j],
                                )
                            )

                if conflicts_present is True:
                    return conflicts
                else:
                    return "No booking conflicts detected in file."
            else:
                return "File provided is empty."
        except IOError:
            return "File could not be read."


if __name__ == "__main__":
    """
    Error handling that ensures an error message is displayed
    if no file path is provided by the user.
    """
    try:
        # Allows the file path to be read via the command line.
        print(CheckBookings(sys.argv[1]).check_bookings())
    except IndexError:
        print("No file path specified.")
        # Program exit due to error.
        sys.exit(1)
