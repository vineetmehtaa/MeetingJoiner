from functions import findLinkAndLaunch
from setup import setup
from sys import argv, exit
import validators

# importing file contents for estimating function calls
config = open("details.txt", "r")
check = config.readlines()
config.close()

# checking if content in "details.txt" is valid for function calls
if len(check) == 3 and check[0][-6:-4] == "PU" and validators.url(check[1]) and validators.url(check[2]):
	findLinkAndLaunch()

# instantiate setup process for "details.txt"
else:
	input("Enter any key to start setup...")
	setup()
