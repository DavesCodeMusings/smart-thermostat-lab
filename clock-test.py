from machine import RTC
from time import sleep

# There's no way to set the clock yet, so we just make up a time for now.
rtc = RTC()
rtc.init((2022, 2, 21, 2, 9, 59, 0, 0))  # 2022, Feb 21 9:59:00 GMT

# Date-Time comes as an array indexed like this...
# 0:year, 1:month, 2:day, 3:day of week 4:hour, 5:minute, 6:second, 7:microsecond, 7:timezone offset
# We're really only interested in hour, minute, and second.
while (1):
  dt = rtc.datetime()
  hour = dt[4]
  minute = dt[5]
  second = dt[6]
  leading_zero_minute = "0" if (minute < 10) else ""  # Stops goofy looking times like 7:0
  leading_zero_second = "0" if (second < 10) else ""
  print(str(hour) + ":" + leading_zero_minute + str(minute) + ":" + leading_zero_second + str(second))
  sleep(1)
