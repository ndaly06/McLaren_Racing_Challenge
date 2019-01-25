# imports the check_bookings program and it's CheckBookings class
from check_bookings import CheckBookings

# imports the unittest test runner library
import unittest

# #
# sum = target.sum

# creates a TestSum subclass of the TestCase class


class Test(unittest.TestCase):

    # 
    def test1(self):
        """
        Tests that the script can handle empty csv files
        If the file is empty, "File is empty or no arguments passed
        """
        filepath = "data/testdata1.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File is empty or no arguments passed")

    # 
    def test2(self):
        """
        Tests that the script can handle empty paths
        If the filepath is empty, "File not found or path is incorrect"
        """
        filepath = ""
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File not found or path is incorrect")

# END Test


#  ensures that the tests are ran as a script
if __name__ == '__main__':
    unittest.main()
