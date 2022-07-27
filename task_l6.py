import datetime
from datetime import timedelta

present_time = datetime.datetime.now()
starting_date = datetime.date(2022, 6, 22)
days = 30


def get_cycles(date):
    first_cycle_end = starting_date + timedelta(days)
    second_cycle_end = starting_date + timedelta(days*2)
    third_cycle_end = starting_date + timedelta(days*3)
    date = date.date()
    days_left = third_cycle_end - date
    return f"First cycle end: {first_cycle_end}, Second cycle end: {second_cycle_end}, Third cycle end: {third_cycle_end}, project defence: {days_left} left!"


print(get_cycles(present_time))

def devide_time(date):
  stage1 = date