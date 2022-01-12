import calendar
from datetime import date
from datetime import datetime
from setup import setup
from sys import argv, exit

# Creating a 'now' object to get H:M:S
now = datetime.now()

# Getting date day and time
date = date.today()
day = calendar.day_name[date.weekday()]
time = float(now.strftime("%H.%M"))

# Category of time(1-8)
time_category = -2

# Finding out the current class number(0-5 indices)
config = open("details.txt", "r")
check = config.readlines()
config.close()

if len(check) == 0:
	setup()
	exit()

if day != "Saturday":
	if time > 12.40 or time < 8.10:
		time_category = -1

	elif time >= 8.10 and time < 9.10:
		time_category = 0

	elif time >= 9.10 and time < 10.00:
		time_category = 1

	elif time >= 10.00 and time < 10.50:
		time_category = 2

	elif time >= 10.50 and time < 11.00:
		time_category = 3

	elif time >= 11.00 and time < 11.50:
		time_category = 4

	elif time >= 11.50 and time < 12.40:
		time_category = 5

else:
	if time > 12.20 or time < 8.10:
		time_category = -1

	elif time >= 8.10 and time < 9.00:
		time_category = 0

	elif time >= 9.00 and time < 9.50:
		time_category = 1

	elif time >= 9.50 and time < 10.40:
		time_category = 2

	elif time >= 10.40 and time < 10.50:
		time_category = 3

	elif time >= 10.50 and time < 11.45:
		time_category = 4

	elif time >= 11.45 and time < 12.20:
		time_category = 5
