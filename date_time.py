import time

print("The epoch on this system starts at " + time.strftime('%c', time.gmtime(0)))
# The epoch on this system starts at Thu Jan  1 00:00:00 1970
print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
# The current timezone is Eastern Standard Time with an offset of 18000

if time.daylight != 0:
    print("\tDaylight Saving Time is in effect for this location")
    #	Daylight Saving Time is in effect for this location

    print("\tThe DST timezone is " + time.tzname[1])
    #	The DST timezone is Eastern Daylight Time


print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#Local time is 2020-10-20 23:02:36

print("UTC time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()))
# UTC time is 2020-10-21 03:02:36
