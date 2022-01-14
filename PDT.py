from base64 import standard_b64encode
import calendar
import time
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

		elif t >= 8.10 and t < 9.10:
			time_category = 0

		elif t >= 9.10 and t < 10.00:
			time_category = 1

		elif t >= 10.00 and t < 10.50:
			time_category = 2

		elif t >= 10.50 and t < 11.00:
			time_category = 3

		elif t >= 11.00 and t < 11.50:
			time_category = 4

		elif t >= 11.50 and t < 12.40:
			time_category = 5

	# Else finding Saturday's timeset
	else:
		if t > 12.20 or t < 8.10:
			time_category = -1

		elif t >= 8.10 and t < 9.00:
			time_category = 0

		elif t >= 9.00 and t < 9.50:
			time_category = 1

		elif t >= 9.50 and t < 10.40:
			time_category = 2

		elif t >= 10.40 and t < 10.50:
			time_category = 3

		elif t >= 10.50 and t < 11.45:
			time_category = 4

		elif t >= 11.45 and t < 12.20:
			time_category = 5

else:
	# checking if day isn't Saturday to get timeset
	if day != "Saturday":
		if t > 12.40 or t < 8.10:
			time_category = -1

		elif t >= 8.10 and t < 9.10:
			time_category = 0

		elif t >= 9.10 and t < 10.00:
			time_category = 1

		elif t >= 10.00 and t < 10.10:
			time_category = 2

		elif t >= 10.10 and t < 11.00:
			time_category = 3

		elif t >= 11.00 and t < 11.50:
			time_category = 4

		elif t >= 11.50 and t < 12.40:
			time_category = 5

	# Else finding Saturday's timeset
	else:
		if t > 12.20 or t < 8.10:
			time_category = -1

		elif t >= 8.10 and t < 9.00:
			time_category = 0

		elif t >= 9.00 and t < 9.50:
			time_category = 1

		elif t >= 9.50 and t < 10.00:
			time_category = 2

		elif t >= 10.00 and t < 10.50:
			time_category = 3

		elif t >= 10.50 and t < 11.45:
			time_category = 4

		elif t >= 11.45 and t < 12.20:
			time_category = 5