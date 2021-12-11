[![Unit Tests Status](https://github.com/nialdaly/mclaren-racing-challenge/workflows/mclaren-racing-challenge-tests/badge.svg)](https://github.com/nialdaly/mclaren-racing-challenge/actions?query=workflow%3Amclaren-racing-challenge-tests)

# McLaren Racing Challenge
Imagine you are provided a file containing a collection of requests to book a particular meeting room; each entry in the file specifies the start time and end time of a meeting. 
We would like you to write a small application that imports the contents of the file and detects whether or not any of the requested bookings conflict.

## Getting Started
A number of assumptions were made when developing this solution:
1. The booking data in the file is related to only 1 meeting room.
2. The files would be in CSV format.
3. The files would contain three columns, namely Request_ID, Start_Time, End_Time.
4. The time is in the 24 hour system format. (HH:MM:SS)

If two meeting requests are made they are stored as follows:

|  Request_ID  |  Start_Time  |   End_Time   |
| ------------ | ------------ | ------------ |
|      1       |   09:00:00   |   12:00:00   |
|      2       |   11:00:00   |   14:00:00   |

The data can be checked as follows:

If meeting 1 starts before meeting 2 ends and meeting 1 ends after meeting 2 starts then a booking conflict has occurred because meeting 2 starts at 11 am which is before meeting 1 is scheduled to end at 12 noon.

Essentially a booking conflict occurs if meeting 1 doesn't end before meeting 2 starts. This logic is applied throughout the booking requests data to identify any conflicts. Based on the data in the table shown, a booking conflict between request 1 and request 2 exists.

`check_bookings.py` can be run in the root of the directory on a specific dataset `conflicts_data1.csv` as shown below:
```
python3 mclaren_racing_challenge/check_bookings.py ./tests/test_data/conflicts_data1.csv
```

## Tests
Tests can be run using _pytest_ in the root of the directory as shown below:
```
pytest
```
