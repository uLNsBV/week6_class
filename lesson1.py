# datetime
import datetime
from datetime import timedelta
# present_time = datetime.datetime.now()
# date_2 = datetime.date(2022, 5, 25)
# timing = datetime.time(14, 34)


# new_time = present_time.date() - date_2


# present_time = datetime.datetime.now()

# days = 30
# end_date = present_time + timedelta(days)


# print(present_time)
# print(present_time.date())
# print(present_time.time())
# print(new_time)
# print(timed)

# print(present_time.strftime('%a'))
# print(date_2.strftime("%a"))

# print(end_date)


present_hour = datetime.datetime.now()
print(present_hour.strftime("%m-%d-%Y %H:%M"))


# WHAT are strf and strp?
# strptime(str, format: %d/%m/%Y %H: %M) --> changes str format into  datetime.datetime
# strftime --> datetime.datetime.now().strftime(%d/%m/%Y %H: %M)  !!!seconds removed!!! to remove specific parts out of a given datetime



