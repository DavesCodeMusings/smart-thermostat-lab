from machine import RTC
from time import sleep

# There's no way to set the clock yet, so we just make up a time for now.
rtc = RTC()
rtc.datetime((2022, 2, 21, 0, 9, 59, 0, 0))  # 2022, Feb 21, Monday 9:59:00

day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Date-Time comes as an array indexed like this...
# 0:year, 1:month, 2:day, 3:day of week 4:hour, 5:minute, 6:second, 7:microsecond
while (1):
  date_time = rtc.datetime()
  date = "{:s}, {:d}/{:d}/{:d}".format(day_of_week[date_time[3]], date_time[1], date_time[2], date_time[0])
  time = "{:d}:{:02d}:{:02d}".format(date_time[4], date_time[5], date_time[6])
  print(date, time)
  sleep(1)
