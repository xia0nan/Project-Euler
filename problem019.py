"""
Author: Nan <xnone0104@gmail.com>

https://projecteuler.net/problem=19


You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

from datetime import date, timedelta


start_date = date(year=1901, month=1, day=1)
end_date = date(year=2000, month=12, day=31)

one_day = timedelta(days=1)

current_day = start_date

count_match = 0

while current_day != end_date:
	if current_day.day == 1 and current_day.weekday() == 6:
		count_match += 1
	current_day += one_day

print(count_match)

# Reference from discussion: https://projecteuler.net/thread=19;page=8
import calendar
print([calendar.weekday(y,m,1) for y in range(1901,2001) for m in range(1,13)].count(6))