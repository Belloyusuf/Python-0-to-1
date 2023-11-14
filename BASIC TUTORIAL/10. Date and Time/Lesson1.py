from datetime import date  # Import date from datetime


# print the current date
now = date.today()
print("Current year and Date is: ", now)


# Print the date of birth 
birth_date = date(1997, 1, 20)  # Date of birth
get_result = now - birth_date
print("I spent " , get_result.days)