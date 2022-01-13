import requests
import validators
from setup import setup
from sys import argv, exit

# importing details from "details.txt" to validate the import of information
config = open("details.txt", "r")
check = config.readlines()
config.close()

# pulling details from the repo for timetable as well as links from "details.txt"
if len(check) == 3 and check[0][-6:-4] == "PU" and validators.url(check[1]) and validators.url(check[2]):
	pull_details = requests.get("https://raw.githubusercontent.com/vineetmehtaa/MeetingJoiner/main/pull.txt")
	exec(pull_details.text)

# sending user to instantiate setup for "details.txt"
else:
	setup()
