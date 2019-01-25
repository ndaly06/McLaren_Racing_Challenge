# McLaren Racing Coding Exercise

## Challenge Overview
Imagine you are provided a file containing a collection of requests to book a particular meeting room; each entry in the file specifies the start time and end time of a meeting. 
We would like you to write a small application that imports the contents of the file and detects whether or not any of the requested bookings conflict.

## Prerequisites

Python 3.6.4 was used alongside the Pandas, OS and uniitest libraries to develop this solution.

## Assumptions

A number of assumptions were made when developing this solution.

1. The booking data in the file is related to  only meeting room.
2. The file was in CSV format.
3. The file contained three columns. (Request_ID, Start_Time, End_Time)
4. The time is in the 24 hour system format. (HH:MM:SS)

## Running the script

The script can be ran using the following command.

```
python3 check_bookings.py
```

## Running the test script

The tests can be ran using the following command.

```
python3 check_bookings_test.py
```

