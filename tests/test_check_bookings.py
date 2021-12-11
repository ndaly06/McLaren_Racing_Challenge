import unittest
from mclaren_racing_challenge.check_bookings import CheckBookings


class Test(unittest.TestCase):
    """
    Creates a TestSum subclass of the TestCase class.
    """

    def test_empty_path(self):
        """
        Tests that the script can handle empty file paths.
        If the filepath is empty, "File could not be read".
        """
        filepath = ""
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(result, "File could not be read.")

    def test_wrong_path(self):
        """
        Tests that the script can handle empty file paths.
        If the filepath is incorrect, "File could not be read".
        """
        filepath = "./tests/test_data/wrongpath.csv"
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(result, "File could not be read.")

    def test_empty_file(self):
        """
        Tests that the script can handle empty files.
        If the filepath is incorrect, "File could not be read".
        """
        filepath = "./tests/test_data/emptyfile.csv"
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(result, "File provided is empty.")

    def test_conflicts1(self):
        """
        Tests that the script can detect if a meeting
        ends during another meeting, which is as a conflict.
        """
        filepath = "./tests/test_data/conflicts_data1.csv"
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(
            result, [("Booking conflict detected between request", 1, "and request", 2)]
        )

    def test_conflicts2(self):
        """
        Tests that the script can detect if a meeting starts during another meeting
        which is as a conflict.
        """
        filepath = "./tests/test_data/conflicts_data2.csv"
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(
            result, [("Booking conflict detected between request", 2, "and request", 3)]
        )

    def test_conflicts3(self):
        """
        Tests that the script can detect if a meeting starts and ends during another meeting
        which is a conflict.
        """
        filepath = "./tests/test_data/conflicts_data3.csv"
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(
            result, [("Booking conflict detected between request", 1, "and request", 2)]
        )

    def test_all_conflicts(self):
        """
        Tests that the script can detect all meeting conflicts present
        file contains 3 meeting conflicts.
        """
        filepath = "./tests/test_data/all_conflicts.csv"
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(
            result,
            [
                ("Booking conflict detected between request", 1, "and request", 2),
                ("Booking conflict detected between request", 1, "and request", 3),
                ("Booking conflict detected between request", 2, "and request", 3),
            ],
        )

    def test_no_conflicts(self):
        """
        Tests that the script can confirm that no meeting conflicts exist
        file contains no meeting conflicts.
        """
        filepath = "./tests/test_data/no_conflicts.csv"
        result = CheckBookings(filepath).check_bookings()
        self.assertEqual(result, "No booking conflicts detected in file.")


if __name__ == "__main__":
    unittest.main()
