# McLaren Racing Coding Exercise

## Challenge Overview
Imagine you are provided a file containing a collection of requests to book a particular meeting room; each entry in the file specifies the start time and end time of a meeting. 
We would like you to write a small application that imports the contents of the file and detects whether or not any of the requested bookings conflict.

## Prerequisites

Python 3.6.4 was used alongside the Pandas, OS, sys and uniitest libraries to develop this solution.

## Assumptions

A number of assumptions were made when developing this solution.

1. The booking data in the file is related to  only meeting room.
2. The file was in CSV format.
3. The file contained three columns. (Request_ID, Start_Time, End_Time)
4. The time is in the 24 hour system format. (HH:MM:SS)

## Solution Logic

If two meeting requests are made they are stored as follows:

|  Request_ID  |  Start_Time  |   End_Time   |
| ------------ | ------------ | ------------ |
|      1       |   09:00:00   |   12:00:00   |
|      2       |   11:00:00   |   14:00:00   |

The data can be checked as follows:

If meeting 1 starts before meeting 2 ends and meeting 1 ends after meeting 2 starts then a booking conflict has occurred because meeting 2 starts at 11 am which is before meeting 1 is scheduled to end at 12 noon.

Essentially a booking conflict occurs if meeting 1 doesn't end before meeting 2 starts.

This logic is applied throughout the booking requests data to identify any conflicts.

Based on the data in the table shown, a booking conflict between request 1 and request 2 exists.

## Test Cases

Can the check_booking program:
1. handle empty files
2. handle incorrect file paths
3. detect if a meeting ends during another meeting (conflict)
4. detect if a meeting starts during another meeting (conflict)
5. detect if a meeting starts and ends during another meeting (conflict)
6. detect every booking conflict in the file
7. determine that no booking conflicts exist

## Running the script

The script can be ran using the following command and by passing in the path of the file that is to be checked as an argument.

```
python3 check_bookings.py "data/testdata3.csv"
```

## Running the test script

The tests can be ran using the following command.

```
python3 check_bookings_tests.py
```