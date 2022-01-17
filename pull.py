import requests
import validators
import base64
from setup import setup
from sys import argv, exit

# checking for internet connection
url = "https://www.google.com/"
timeout = 5
try:
	request = requests.get(url, timeout=timeout)
except (requests.ConnectionError, requests.Timeout) as exception:
	input("No internet connection! Try again!")
	exit()

# importing details from "details.txt" to validate the import of information
config = open("details.txt", "r")
check = config.readlines()
config.close()

# pulling details from the repo for timetable as well as links from "details.txt"
if len(check) == 3 and check[0][-6:-4] == "PU" and validators.url(check[1]) and validators.url(check[2]):
	pull_details = requests.get("https://raw.githubusercontent.com/vineetmehtaa/MeetingJoiner/main/pulling.txt")
	exec(base64.b64decode(pull_details.text).decode('utf-8'))

# sending user to instantiate setup for "details.txt"
else:
	setup()

kkc = open("version.txt", "r")
if kkc.read() != version:
	print("There is an update!")
	input("Download the new version from: https://github.com/vineetmehtaa/MeetingJoiner")
	exit()
kkc.close()