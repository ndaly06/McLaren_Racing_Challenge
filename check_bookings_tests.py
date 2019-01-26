# imports the check_bookings program and it's CheckBookings class
from check_bookings import CheckBookings

# imports the unittest test runner library
import unittest

# creates a TestSum subclass of the TestCase class


class Test(unittest.TestCase):

    #
    def test1(self):
        """
        Tests that the script can handle empty file paths
        If the filepath is empty, "File could not be read"
        """
        filepath = ""
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File could not be read")

    #
    def test2(self):
        """
        Tests that the script can handle incorrect file paths
        If the filepath is incorrect, "File could not be read"
        """
        filepath = "data/test.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File could not be read")

    #
    def test3(self):
        """
        Does meeting 1 end within meeting 2

        """
        filepath = "data/testdata3.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 2)])

    #
    def test4(self):
        """
        Tests that the script can

        does a meeting start within another meeting
        Meeting 2 starts before meeting 2 ends
        """
        filepath = "data/testdata4.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(
            result, [('Booking conflict detected between request', 2, 'and request', 3)])

    #
    def test5(self):
        """
        Tests that the script can detect if a meeting starts and ends during another meeting
        """
        filepath = "data/testdata5.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 2)])


# END Test

#  ensures that the tests are ran as a script
if __name__ == '__main__':
    unittest.main()
