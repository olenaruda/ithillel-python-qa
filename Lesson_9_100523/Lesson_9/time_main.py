import time

# time.sleep(4)  # дуже погана штука

# localtime = time.localtime()
# print(localtime)
#
# # time.struct_time(tm_year=2023, tm_mon=5, tm_mday=10, tm_hour=20, tm_min=8, tm_sec=4, tm_wday=2, tm_yday=130, tm_isdst=1)
# # tuple де є інформація про поточний час
#
# print(localtime.tm_zone)  # EEST
#
#
# mktime = time.mktime(localtime)  # дата трансформується у таймстемп
# print(mktime)

# my_date_tuple = (2022, 12, 12, 20, 30, 15, 11, 340, 1)
# mktime_tuple = time.mktime(my_date_tuple)
# print(mktime_tuple)  # 1670866215.0

#
# print(time.asctime())  # Wed May 10 20:13:33 2023 - принтить поточну дату
# my_date_tuple = (2022, 12, 12, 20, 30, 15, 11, 340, 1)
# (time.asctime(my_date_tuple))  # Fri Dec 12 20:30:15 2022

# my_date_tuple = (2022, 12, 12, 20, 30, 15, 11, 340, 1)
# localtime = time.localtime()
# time_string = time.strftime("My date %m/%d/%Y, %H:%M:%S", my_date_tuple)  # My date 12/12/2022, 20:30:15
# print(time_string)

my_date = "15 June, 2023, 20:22:40"
result = time.strptime(my_date, "%d %B, %Y, %H:%M:%S")
print(result)
print(type(result))

print(time.asctime(result))

# '{}'.format('1')

