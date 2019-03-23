import datetime

yesterday = datetime.date(2018, 5, 2)
current_time = datetime.time(16, 25, 45)
another_time = datetime.time(16, 25, 45)
if current_time == another_time:
    print('Ok')
