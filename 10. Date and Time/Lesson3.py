from datetime import date


#  Return a date corresponding to a date_string given in any valid 
#  ISO 8601 format, except ordinal dates (e.g. YYYY-DDD):

valid_date1 = date.fromisoformat('2020-12-04')
print("Valid date 1", valid_date1)

valid_date2 = date.fromisoformat('20201204')
print("Valid date 2", valid_date2)

valid_date3 = date.fromisoformat('2020-W01-04')
print("valid date 3", valid_date3)



# Replace day
day = date(2020, 12, 30)
rep_day = d.replace(day=22)
print(rep_day)

# ISO Format 
date_format = date(2002, 12, 4).isoformat()
print(date_format)

# date.ctime()
#  Return a string representing the date:
ct = date(2002, 12, 4).ctime() 
print(ct)

# ct.ctime() is equivalent to: 
# time.ctime(time.mktime(d.timetuple()))

