"""util functions for broadcast calendar

   https://en.wikipedia.org/wiki/Broadcast_calendar
"""

from datetime import date, timedelta


def broadcast_month_start(year, month):
    """return start date of broadcast month. always on monday"""
    start_date = date(year, month, 1)
    while start_date.weekday() != 0:
        start_date -= timedelta(days=1)
    return start_date

def quarter_start_month(quarter):
    """month that starts quarter for Gregorian calendar: Jan, Apr, Jul, Oct"""
    if quarter not in range(1, 5):
        raise ValueError("invalid quarter")
    return {1: 1, 2: 4, 3: 7, 4: 10}[quarter]
    # return 3 * quarter - 2

def get_quarter(month):
    """return quarter for month"""
    if month not in range(1, 13):
        raise ValueError("invalid month")
    return {1: 1, 2: 1, 3: 1,
            4: 2, 5: 2, 6: 2,
            7: 3, 8: 3, 9: 3,
            10: 4, 11: 4, 12: 4}[month]
    # return (month + 2) // 3

def next_quarter(year, quarter, num=1):
    """return next quarter for Gregorian calendar"""
    if quarter not in range(1, 5):
        raise ValueError("invalid quarter")
    quarter -= 1 # for mod, div
    quarter += num
    year += quarter // 4
    quarter %= 4
    quarter += 1 # back
    return year, quarter

def broadcast_quarter_dates(year, quarter, length=1):
    """start and end dates for broadcast quarter"""
    month = quarter_start_month(quarter)
    start = broadcast_month_start(year, month)

    # calculate end of quarter based on start of subsequent quarter
    year, quarter = next_quarter(year, quarter, length)
    month = quarter_start_month(quarter)
    end = broadcast_month_start(year, month) - timedelta(days=1)

    return start, end

def next_quarter_broadcast_dates(length=1, start_offset=0, end_offset=0):
    """return dates for next broadcast quarter (from now)"""
    now = date.today()
    year = now.year
    quarter = get_quarter(now.month)

    while True:
        start, end = broadcast_quarter_dates(year, quarter, length)
        if now < start:
            break
        year, quarter = next_quarter(year, quarter)

    return (start+timedelta(days=start_offset),
            end+timedelta(days=end_offset))


def get_broadcast_weeks(start, end):
    """return broadcast weeks for date range"""

    weeks = []
    temp = start
    if start <= end:
        while temp.weekday() != 0:
            temp -= timedelta(days=1)
        while temp <= end:
            weeks.append(temp)
            temp += timedelta(days=7)
    return weeks
