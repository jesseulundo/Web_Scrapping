import sys
import datetime
from datetime import date
January = 1
February = 2
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def weekday(year, month, day):
		
	return datetime.date(year, month, day).weekday()
	
def isleap(year):
		
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
	if not 1 <= month <= 12:
		pass
	day1 = weekday(year, month, 1)
	ndays = mdays[month] + (month == February and isleap(year))
	return ndays
print(days_in_month(2012, 2))

#ndays = mdays[month] + (month == February and isleap(year))
def is_valid_date(year, month, day):
	#ndays = mdays[month] + (month == February and isleap(year))
	if datetime.MINYEAR <= year <= datetime.MAXYEAR:
		if 1 <= month <=12:
			if 1 <= day <= 31 and 1 <= day <= ndays:
				return True
			else: return False
	else: return False
				
print(is_valid_date(1990, 12, 3))


 
def days_between(year1, month1, day1, year2, month2, day2):
	date1 = date(year1, month1, day1)
	date2 = date(year2, month2, day2)
	try:
		diff = date2 - date1
		if is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2):
			return diff
	except:
		if date2 < date1:
			return 0
	else:
		return 0
		
print(days_between(2014, 5, 5, 2014, 5, 6))

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    return 0
