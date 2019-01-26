# imports the check_bookings program and it's CheckBookings class
from check_bookings import CheckBookings

# imports the unittest test runner library
import unittest

# creates a TestSum subclass of the TestCase class


class Test(unittest.TestCase):

    #
    def test_empty_path(self):
        """
        Tests that the script can handle empty file paths
        If the filepath is empty, "File could not be read"
        """
        filepath = ""
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File could not be read")
    
    def test_wrong_path(self):
        """
        Tests that the script can handle empty file paths
        If the filepath is incorrect, "File could not be read"
        """
        filepath = "data/wrongpath.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File could not be read")

    #
    def test_empty_file(self):
        """
        Tests that the script can handle empty files
        If the filepath is incorrect, "File could not be read"
        """
        filepath = "data/emptyfile.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(result, "File provided is empty")

    #
    def test3(self):
        """
        Tests that the script can detect if a meeting ends during another meeting 
        which is as a conflict
        """
        filepath = "data/testdata3.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 2)])

    #
    def test4(self):
        """
        Tests that the script can detect if a meeting starts during another meeting 
        which is as a conflict
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
        which is a conflict
        """
        filepath = "data/testdata5.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 2)])

    #
    def test6(self):
        """
        Tests that the script can detect all meeting conflicts present
        testdata6.csv contains 2 meeting conflicts
        """
        filepath = "data/testdata6.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 3),
            ('Booking conflict detected between request', 4, 'and request', 5)])

    
    def test7(self):
        """
        Tests that the script can confirm that no meeting conflicts exist
        testdata7.csv contains no meeting conflicts
        """
        filepath = "data/testdata7.csv"
        result = CheckBookings(filepath).check_bookings()
        #
        self.assertEqual(
            result, "No booking conflicts detected in file")


# END Test

#  ensures that the tests are ran as a script
if __name__ == '__main__':
    unittest.main()
