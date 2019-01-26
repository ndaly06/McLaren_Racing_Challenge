# imports the unittest test runner library
import unittest
# imports the check_bookings program and it's CheckBookings class
from check_bookings import CheckBookings

# creates a TestSum subclass of the TestCase class


class Test(unittest.TestCase):

    def test_empty_path(self):
        """
        Tests that the script can handle empty file paths
        If the filepath is empty, 'File could not be read'
        """
        filepath = ''
        result = CheckBookings(filepath).check_bookings()
        
        self.assertEqual(result, 'File could not be read')

    def test_wrong_path(self):
        """
        Tests that the script can handle empty file paths
        If the filepath is incorrect, 'File could not be read'
        """
        filepath = 'data/wrongpath.csv'
        result = CheckBookings(filepath).check_bookings()
        
        self.assertEqual(result, 'File could not be read')

    def test_empty_file(self):
        """
        Tests that the script can handle empty files
        If the filepath is incorrect, 'File could not be read'
        """
        filepath = 'data/emptyfile.csv'
        result = CheckBookings(filepath).check_bookings()
        
        self.assertEqual(result, 'File provided is empty')

    def test_conflicts1(self):
        """
        Tests that the script can detect if a meeting ends during another meeting 
        which is as a conflict
        """
        filepath = 'data/conflicts_data1.csv'
        result = CheckBookings(filepath).check_bookings()
        
        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 2)])

    def test_conflicts2(self):
        """
        Tests that the script can detect if a meeting starts during another meeting 
        which is as a conflict
        """
        filepath = 'data/conflicts_data2.csv'
        result = CheckBookings(filepath).check_bookings()
        
        self.assertEqual(
            result, [('Booking conflict detected between request', 2, 'and request', 3)])

    def test_conflicts3(self):
        """
        Tests that the script can detect if a meeting starts and ends during another meeting
        which is a conflict
        """
        filepath = 'data/conflicts_data3.csv'
        result = CheckBookings(filepath).check_bookings()

        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 2)])

    def test_all_conflicts(self):
        """
        Tests that the script can detect all meeting conflicts present
        testdata6.csv contains 3 meeting conflicts
        """
        filepath = 'data/all_conflicts.csv'
        result = CheckBookings(filepath).check_bookings()
        
        self.assertEqual(
            result, [('Booking conflict detected between request', 1, 'and request', 2), 
                    ('Booking conflict detected between request', 1, 'and request', 3),
                    ('Booking conflict detected between request', 2, 'and request', 3)
                    ])

    def test_no_conflicts(self):
        """
        Tests that the script can confirm that no meeting conflicts exist
        testdata7.csv contains no meeting conflicts
        """
        filepath = 'data/no_conflicts.csv'
        result = CheckBookings(filepath).check_bookings()
        
        self.assertEqual(
            result, 'No booking conflicts detected in file')


# END Test

#  ensures that the tests are ran as a script
if __name__ == '__main__':
    unittest.main()
