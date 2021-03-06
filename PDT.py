import calendar
import time
import validators
from datetime import date
from datetime import datetime
from setup import setup
from sys import argv, exit
from pull import *

# Creating a 'now' object to get H:M:S
now = datetime.now()

# Getting date day and time
date = date.today()
day = calendar.day_name[date.weekday()]
t = float(now.strftime("%H.%M"))

# Category of time(0-5 = 6[consider subscripts])
time_category = -1

# Finding out the current class number(0-5 indices)
config = open("details.txt", "r")
check = config.readlines()
config.close()

# checking if the file is empty
if len(check) != 3:
	setup()
	exit()

standard = check[0][5:8]

if standard == "PU2":
	# checking if day isn't Saturday to get timeset
	if day != "Saturday":
		if t > 12.40 or t < 8.10:
			time_category = -1

		if t >= 8.10 and t < 9.10:
			time_category = 0

		if t >= 9.10 and t < 10.00:
			time_category = 1

		if t >= 10.00 and t < 10.50:
			time_category = 2

		if t >= 10.50 and t < 11.00:
			time_category = 3

		if t >= 11.00 and t < 11.50:
			time_category = 4

		if t >= 11.50 and t < 12.40:
			time_category = 5

		if "ABC".find(section[-1]) != -1 and t >= 18.00 and t < 18.50:
			time_category = 6

	# Else finding Saturday's timeset
	else:
		if t > 12.20 or t < 8.10:
			time_category = -1

		if t >= 8.10 and t < 9.00:
			time_category = 0

		if t >= 9.00 and t < 9.50:
			time_category = 1

		if t >= 9.50 and t < 10.40:
			time_category = 2

		if t >= 10.40 and t < 10.50:
			time_category = 3

		if t >= 10.50 and t < 11.45:
			time_category = 4

		if t >= 11.45 and t < 12.20:
			time_category = 5

else:
	# checking if day isn't Saturday to get timeset
	if day != "Saturday":
		if t > 12.40 or t < 8.10:
			time_category = -1

		if t >= 8.10 and t < 9.10:
			time_category = 0

		if t >= 9.10 and t < 10.00:
			time_category = 1

		if t >= 10.00 and t < 10.10:
			time_category = 2

		if t >= 10.10 and t < 11.00:
			time_category = 3

		if t >= 11.00 and t < 11.50:
			time_category = 4

		if t >= 11.50 and t < 12.40:
			time_category = 5

		if "ABC".find(section[-1]) != -1 and t >= 18.00 and t < 18.50:
			time_category = 6

	# Else finding Saturday's timeset
	else:
		if t > 12.20 or t < 8.10:
			time_category = -1

		if t >= 8.10 and t < 9.00:
			time_category = 0

		if t >= 9.00 and t < 9.50:
			time_category = 1

		if t >= 9.50 and t < 10.00:
			time_category = 2

		if t >= 10.00 and t < 10.50:
			time_category = 3

		if t >= 10.50 and t < 11.45:
			time_category = 4

		if t >= 11.45 and t < 12.20:
			time_category = 5