from datetime import date  # Import date from datetime
import time  


# print the current date
now = date.today()
print("Current year and Date is: ", now)


# Print the date of birth 
birth_date = date(1997, 1, 20)  # Date of birth
get_result = now - birth_date
print("I spent " , get_result.days)


# Print current time
localtime = time.localtime(time.time())
print("Local current time is: ", localtime)


# Getting formatted time
# TODO
"""
You can format any time as per your requirement, but a simple method to get time in a
readable format is asctime() 
------------------ 
The method asctime() converts a tuple or struct_time representing a time as returned by
gmtime() or localtime() 
"""
formated_time = time.asctime(time.localtime(time.time()))
print("Formated time is: ", formated_time)