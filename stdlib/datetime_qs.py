from datetime import date, datetime, timedelta, timezone


# date(year, month, day), naive
today = date.today()
print(f'today: {repr(today)} {today.isoformat()}')
# date -> datetime.  for datetime -> date, use datetime.date()
print(f'as datetime: {datetime(today.year, today.month, today.day)}')
print(f'from POSIX ts 1535986578: {date.fromtimestamp(1535986578)}')
# print(f'from 2018-09-03: {repr(date.fromisoformat("2018-09-03"))}')


# datetime
print(f'Aware current UTC datetime: {datetime.now(timezone.utc).isoformat()}')
print(f'same from POSIX ts 1535986578: {datetime.fromtimestamp(1535986578, timezone.utc)}')
# print(f'{datetime.fromisoformat("2018-09-03T11:50:06.788398-04:00")}')
print(f'POSIX ts from naive, current, local dt: {datetime.now().timestamp()}')


# timedelta
print(f'# seconds in an hour: {timedelta(hours=1).total_seconds()}')
print(f'5 days from today: {today + timedelta(days=5)}')
dt1 = datetime(2019, 2, 17, 12, 30, 28, 990000)
dt2 = datetime(2019, 2, 17, 12, 30, 29, 115000)
print(f'{dt2} - {dt1}: {dt2 - dt1}  seconds delta: {(dt2-dt1).total_seconds()}')
print(f'{dt1} - {dt2}: {dt1 - dt2}  seconds delta: {(dt1-dt2).total_seconds()}')


# strftime, strptime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
dt_str = '31/10/2016 07:30:00 PM'
fmt = '%d/%m/%Y %I:%M:%S %p'
print(f'{dt_str} parsed using {fmt}: {datetime.strptime(dt_str, fmt)}')
print(f'Naive, current, local dt using {fmt}: {datetime.now().strftime(fmt)}')
