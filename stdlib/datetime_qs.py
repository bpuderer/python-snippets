from datetime import date, datetime, timedelta, timezone


# date(year, month, day), naive
print(f'today: {repr(date.today())} {date.today().isoformat()}')
print(f'from POSIX ts 1535986578: {date.fromtimestamp(1535986578)}')
# print(f'from 2018-09-03: {repr(date.fromisoformat("2018-09-03"))}')


# datetime
print(f'Aware current UTC datetime: {datetime.now(timezone.utc).isoformat()}')
print(f'same from POSIX ts 1535986578: {datetime.fromtimestamp(1535986578, timezone.utc)}')
# print(f'{datetime.fromisoformat("2018-09-03T11:50:06.788398-04:00")}')
print(f'POSIX ts from naive, current, local dt: {datetime.now().timestamp()}')


# timedelta
print(f'# seconds in an hour: {timedelta(hours=1).total_seconds()}')
print(f'5 days from today: {date.today() + timedelta(days=5)}')
d1 = datetime(2018, 9, 3, 12, 30)
d2 = datetime(2017, 10, 23, 9)
print(f'{d1} - {d2}: {d1 - d2}')


# strftime, strptime
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
dt_str = '31/10/2016 07:30:00 PM'
fmt = '%d/%m/%Y %I:%M:%S %p'
print(f'{dt_str} parsed using {fmt}: {datetime.strptime(dt_str, fmt)}')
print(f'Naive, current, local dt using {fmt}: {datetime.now().strftime(fmt)}')
