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
        If the file is empty, "File provided is empty"
        """
        filepath = "data/testdata1.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File provided is empty")

    # 
    def test2(self):
        """
        Tests that the script can handle empty file paths
        If the filepath is empty/incorrect, "File could not be read"
        """
        filepath = ""
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File could not be read")

    # 
    def test3(self):
        """
        Tests that the script can handle incorrect file paths
        If the filepath is incorrect, "File could not be read"
        """
        filepath = "data/testda.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File could not be read")

# END Test


#  ensures that the tests are ran as a script
if __name__ == '__main__':
    unittest.main()