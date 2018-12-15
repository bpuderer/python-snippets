"""util functions for broadcast calendar

   https://en.wikipedia.org/wiki/Broadcast_calendar
"""

from datetime import date, timedelta


def broadcast_week_start(d):
    """return start of broadcast week from date. always on monday"""
    while d.weekday() != 0:
        d -= timedelta(days=1)
    return d

def broadcast_month_start(year, month):
    """return start date of broadcast month"""
    return broadcast_week_start(date(year, month, 1))

def quarter_start_month(quarter):
    """month that starts quarter for Gregorian calendar: Jan, Apr, Jul, Oct"""
    if quarter not in range(1, 5):
        raise ValueError('invalid quarter')
    return {1: 1, 2: 4, 3: 7, 4: 10}[quarter]
    # return 3 * quarter - 2

def quarter_for_month(month):
    """return quarter for month"""
    if month not in range(1, 13):
        raise ValueError('invalid month')
    return {1: 1, 2: 1, 3: 1,
            4: 2, 5: 2, 6: 2,
            7: 3, 8: 3, 9: 3,
            10: 4, 11: 4, 12: 4}[month]
    # return (month + 2) // 3

def next_quarter(year, quarter, num=1):
    """return next quarter for Gregorian calendar"""
    if quarter not in range(1, 5):
        raise ValueError('invalid quarter')
    quarter -= 1 # for mod, div
    quarter += num
    year += quarter // 4
    quarter %= 4
    quarter += 1 # back
    return year, quarter

def broadcast_quarter_dates(year, quarter, num=1, start_offset=0, end_offset=0):
    """start and end dates for broadcast quarter"""
    if num < 1:
        raise ValueError('num must be >= 1')
    month = quarter_start_month(quarter)
    start = broadcast_month_start(year, month)

    # calculate end of quarter based on start of subsequent quarter
    year, quarter = next_quarter(year, quarter, num=num)
    month = quarter_start_month(quarter)
    end = broadcast_month_start(year, month) - timedelta(days=1)

    return start + timedelta(days=start_offset), end + timedelta(days=end_offset)

def next_quarter_broadcast_dates(num=1, start_offset=0, end_offset=0):
    """
       return dates for *next* broadcast quarter (from now)
       with start offset taken into consideration
    """
    now = date.today()
    year = now.year
    quarter = quarter_for_month(now.month)

    while True:
        start, end = broadcast_quarter_dates(year, quarter, num=num,
                                             start_offset=start_offset,
                                             end_offset=end_offset)
        if now < start:
            break
        year, quarter = next_quarter(year, quarter)

    return start, end

def broadcast_week_starts(start, end):
    """return broadcast week starts for date range"""
    weeks = []
    temp = start
    if start <= end:
        temp = broadcast_week_start(temp)
        while temp <= end:
            weeks.append(temp)
            temp += timedelta(days=7)
    return weeks

def broadcast_weeks(start, end):
    """return broadcast weeks with start, end for date range"""
    starts = broadcast_week_starts(start, end)
    return [(start, start+timedelta(days=6)) for start in starts]
