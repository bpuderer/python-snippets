from broadcast_cal_utils import broadcast_quarter_dates, next_quarter_broadcast_dates

for year in range(2018, 2023):
    for quarter in range(1, 5):
        start, end = broadcast_quarter_dates(year, quarter)
        print(start.isoformat(), end.isoformat())

print("NEXT:", next_quarter_broadcast_dates())
print("NEXT 2:", next_quarter_broadcast_dates(2))
print("NEXT 4 shifted -3, 1:", next_quarter_broadcast_dates(4, -3, 1))
