from base64 import standard_b64encode
import calendar
import validators
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

	# Else finding Saturday's timeset
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

else:
	# checking if day isn't Saturday to get timeset
	if day != "Saturday":
		if time > 12.40 or time < 8.10:
			time_category = -1

		elif time >= 8.10 and time < 9.10:
			time_category = 0

		elif time >= 9.10 and time < 10.00:
			time_category = 1

		elif time >= 10.00 and time < 10.10:
			time_category = 2

		elif time >= 10.10 and time < 11.00:
			time_category = 3

		elif time >= 11.00 and time < 11.50:
			time_category = 4

		elif time >= 11.50 and time < 12.40:
			time_category = 5

	# Else finding Saturday's timeset
	else:
		if time > 12.20 or time < 8.10:
			time_category = -1

		elif time >= 8.10 and time < 9.00:
			time_category = 0

		elif time >= 9.00 and time < 9.50:
			time_category = 1

		elif time >= 9.50 and time < 10.00:
			time_category = 2

		elif time >= 10.00 and time < 10.50:
			time_category = 3

		elif time >= 10.50 and time < 11.45:
			time_category = 4

		elif time >= 11.45 and time < 12.20:
			time_category = 5

day = "Monday"
time_category = 2