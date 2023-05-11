import os.path
import datetime
from datetime import date

# NOTES

# lesson 7 task
#
# try:
#     if os.path.exists('file.txt'):
#         pass
#     else:
#
#     my_dict = { path : ""}
# except KeyboardInterrupt:
#     with


# Datetime  --------------------------

# now = datetime.datetime.now()
#
# print(now)  # 2023-05-10 19:38:24.415042
#
# current_date = date.today()
# current_date_2 = datetime.date.today()  # when we don't use import "from datetime import date"
#
# print(current_date)  # 2023-05-10

# current_datetime = datetime.datetime.now()
# current_time = current_datetime.time()
# print(current_time)  # 19:43:39.206765
# print(type(current_time))  # <class 'datetime.time'>
#
# time_obj = datetime.time(12, 35, 20)  # 12:00:00
# print(time_obj)
#
# date_obj = datetime.datetime(2022, 13, 20, 15, 20, 20)  # 2022-10-20 00:00:00
# print(date_obj)

# date_obj = datetime.datetime(2022, 13, 20, 15, 20, 20)  # ValueError: month must be in 1..12

# date_1 = datetime.datetime(2022, 10, 20, 15, 20, 20)
# date_2 = datetime.datetime(2022, 12, 20, 15, 10, 20)
#
# delta = date_2 - date_1
# print(delta)  # 60 days, 23:50:00

# date_1 = datetime.date(2022, 10, 20)
# date_2 = datetime.date(2022, 12, 20)
#
# delta = date_2 - date_1
# print(delta)  # 61 days, 0:00:00

#
# date_1 = datetime.datetime(2022, 10, 20, 15, 20, 20)
date_2 = datetime.datetime(2022, 12, 20, 15, 10, 20)
#
# if date_2 > date_1:
#     print("Hello!")

#
# today = datetime.date.today()
# next_week = today + datetime.timedelta(minutes=7)
#
# print(next_week)


today = datetime.date.today()
print(f'Our date {date_2}')
next_week = date_2 + datetime.timedelta(minutes=7)
print(f'After 7 minutes {next_week}')


print(datetime.datetime.timestamp(date_2))
