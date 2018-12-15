from broadcast_cal_utils import broadcast_quarter_dates, next_quarter_broadcast_dates

for year in range(2018, 2023):
    for quarter in range(1, 5):
        start, end = broadcast_quarter_dates(year, quarter)
        print(f'{year} Q{quarter}: {start.isoformat()} {end.isoformat()}')
    print('---')
