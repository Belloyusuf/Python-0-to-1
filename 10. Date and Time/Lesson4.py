import calendar


"""
The calendar module gives a wide range of methods to play with yearly and monthly
calendars. Here, we print a calendar for a given month ( Jan 2020 ).
"""
cal = calendar.month(2020, 11)
print ("Here is the calendar:")
print (cal)

"""
Something similar to this would be printed

   November 2020
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29


"""