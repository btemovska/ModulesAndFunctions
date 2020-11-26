import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
#The time in Europe/Moscow is 2020-11-27 02:38:39.677819+03:00
print("UTC is {}".format(datetime.datetime.utcnow()))
#UTC is 2020-11-26 23:38:39.677819

# for x in pytz.all_timezones:
#     print(x)  #prints all main cities
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])
# # ZA: South Africa
# # ZM: Zambia
# # ZW: Zimbabwe

for x in sorted(pytz.country_names):
    print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))
# YT: Mayotte: ['Indian/Mayotte']
# ZA: South Africa: ['Africa/Johannesburg']
# ZM: Zambia: ['Africa/Lusaka']
# ZW: Zimbabwe: ['Africa/Harare']

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=':')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")
#actual current time for each zone
# ZA: South Africa:		Africa/Johannesburg: 2020-11-27 01:53:00.357691+02:00
# ZM: Zambia:		Africa/Lusaka: 2020-11-27 01:53:00.357691+02:00
# ZW: Zimbabwe:		Africa/Harare: 2020-11-27 01:53:00.357691+02:00






