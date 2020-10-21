#Write a small program to display information on the
#four clocks whose functions
#i.e. time(), per_counter(), monitonic() and process_time()
#Use the documentation for the get_clock_info() function
#to work out how to call it for each of the clocks

import time
print("time():\t\t\t", time.get_clock_info('time'))
#time(): namespace(adjustable=True, implementation='GetSystemTimeAsFileTime()',
# monotonic=False, resolution=0.015625)

print("perf_counter():\t", time.get_clock_info('perf_counter'))
# perf_counter():	 namespace(adjustable=False,
# implementation='QueryPerformanceCounter()', monotonic=True, resolution=1e-07)

print("monotonic():\t", time.get_clock_info('monotonic'))
# monotonic():	 namespace(adjustable=False, implementation='GetTickCount64()',
# monotonic=True, resolution=0.015625)

print("process_time():\t\t\t", time.get_clock_info('process_time'))
# process_time():			 namespace(adjustable=False,
# implementation='GetProcessTimes()', monotonic=True, resolution=1e-07)

