"""
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""
import datetime
import calendar

def days_in_month(year, month):
    """
    Inputs:
        year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
            representing the year
        month - an integer between 1 and 12 representing the month

    Returns:
        The number of days in the input month.
    """
    if datetime.MINYEAR <= year <= datetime.MAXYEAR:
        if 1 <= month <= 12:
            day = calendar.monthrange(year, month)
            return day[1]
        else: return 0

def is_valid_date(year, month, day):
    """
    Inputs:
        year  - an integer representing the year
        month - an integer representing the month
        day - an integer representing the day

    Returns:
        True if year-month-day is a valid date and
        False otherwise
    """ 
    try:
        days = calendar.monthrange(year, month)
        days1 = days[1]
        if datetime.MINYEAR <= year <= datetime.MAXYEAR:
            if 1<= month <= 12:
                if 1<= day <= days1:	
                    return True
                else:		
                    return False
        else: return False
    except ValueError:
        return False

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
        year1  - an integer representing the year of the first date
        month1 - an integer representing the month of the first date
        day1   - an integer representing the day of the first date
        year2  - an integer representing the year of the second date
        month2 - an integer representing the month of the second date
        day2   - an integer representing the day of the second date

    Returns:
        The number of days from the first date to the second date.
        Returns 0 if either date is invalid or the second date is
        before the first date.
    """
    try:
        date1= datetime.date(year1, month1, day1)
        date2= datetime.date(year2, month2, day2)
        dif = date2 - date1
        diff = dif.days
        if diff < 0:
            return 0
        
    except ValueError:
        return 0
    else: 
        return diff

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
    try:
        today = datetime.date.today()
        dtob = datetime.date(year, month, day)
        age_days = today-dtob 
        if age_days.days < 0:
            return 0
        else:
            return age_days.days
    except ValueError:
        return 0