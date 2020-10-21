import time

print(time.gmtime(0))  # 0 is default oldest date
# time.struct_time(tm_year=1970,
# tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)

print(time.localtime())  # no arguments passed thus it takes today's date
# time.struct_time(tm_year=2020,
# tm_mon=10, tm_mday=20, tm_hour=22, tm_min=28, tm_sec=23, tm_wday=1, tm_yday=294,
# tm_isdst=1)

print(time.time())  # number of seconds since the first of 1970
# 1603247303.650089

print()

time_here = time.localtime()
print(time_here)
# time.struct_time(tm_year=2020, tm_mon=10,
# tm_mday=20, tm_hour=22, tm_min=33, tm_sec=20, tm_wday=1, tm_yday=294, tm_isdst=1)
print("Year:", time_here[0], time_here.tm_year)  # Year: 2020 2020
print("Month:", time_here[1], time_here.tm_mon)  # Month: 10 10
print("Day:", time_here[2], time_here.tm_mday)  # Day: 20 20

print()
#measure how fast you press enter after it tells you when to press enter
from time import time as my_timer
import random

input("Please enter to start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Please enter to stop ")
end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time))) #Started at 22:39:47
print("Ended at " + time.strftime("%X", time.localtime(end_time))) #Ended at 22:39:49
print("Your reaction time was {} seconds ".format(end_time - start_time)) #Your reaction time was 1.9579870700836182 seconds


