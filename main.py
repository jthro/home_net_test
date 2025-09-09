from ping3 import ping
from time import localtime, asctime, sleep
from calendar import month_name

MONTHS_RUNTIME = 3

# host - string, host to ping
# f - file, csv to log to
# tm - time struct (current time)
def ping_dest(host, f, tm):
    latency = ping(host)
    f.write(f"{host},{tm.tm_year},{tm.tm_mon},{tm.tm_mday},{tm.tm_hour},{tm.tm_min},{latency}\n")

# return if current time is the end time
def is_end_time(tm, end_tm):
    return tm.tm_year >= end_tm["year"] and \
           tm.tm_mon >= end_tm["month"] and \
           tm.tm_mday >= end_tm["day"] and \
           tm.tm_hour >= end_tm["hour"] and \
           tm.tm_min >= end_tm["min"]


# ENTRYPOINT
start_time = localtime()

end_time = {
    "year": start_time.tm_year,
    "month": start_time.tm_mon,
    "day": start_time.tm_mday,
    "hour": start_time.tm_hour,
    "min": start_time.tm_min,
}

hosts = [ "google.com", "youtube.com", "aarnet.edu.au", "unsw.edu.au" ]

# if start_time.tm_mon > (12 - MONTHS_RUNTIME):
#     end_time["year"] = start_time.tm_year + 1
# end_time["month"] = start_time.tm_mon + MONTHS_RUNTIME
end_time["month"] = start_time.tm_mon
end_time["year"] = start_time.tm_year
end_time["min"] = start_time.tm_min + 2

print(f"Program started at {asctime(start_time)}, will finish on {end_time['day']} of {month_name[end_time['month']]}, {end_time['year']}")
print(asctime(start_time))

with open("ping_data.csv", "a") as f:
    f.write("host,year,month,day,hour,minute,latency_ms\n")
    curr_time = localtime()
    while not is_end_time(curr_time, end_time):
        for host in hosts:
            ping_dest(host, f, curr_time)
        sleep(10)
        curr_time = localtime()
