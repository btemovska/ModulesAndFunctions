import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time)) #Naive local time 2020-11-26 19:00:33.587355
print("Naive UTC {}".format(utc_time)) #Naive UTC 2020-11-27 00:00:33.587355

aware_local_time = pytz.utc.localize(local_time)
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time {}, time zone {}".format(aware_local_time, aware_local_time.tzinfo))
#Aware local time 2020-11-26 19:03:25.964985+00:00, time zone UTC
print("Aware UTC {}, time zone {}".format(aware_utc_time, aware_utc_time.tzinfo))
# Aware UTC 2020-11-27 00:03:25.964985+00:00, time zone UTC

gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time) #2015-10-25 01:30:00
print(gap_time.timestamp()) #1445751000.0
s = 1445751000
t = s + (60 * 60)
gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)
print("{} seconds since the epoch is {}".format(s, dt1))
#1445751000 seconds since the epoch is 2015-10-25 05:30:00+00:00
print("{} seconds since the epoch is {}".format(s, dt2))
#1445751000 seconds since the epoch is 2015-10-25 06:30:00+00:00



