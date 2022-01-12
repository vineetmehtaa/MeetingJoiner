from functions import findLinkAndLaunch
from setup import setup
from sys import argv, exit
import validators

config = open("details.txt", "r")
check = config.readlines()
config.close()

if len(check) == 3 and check[0][-6:-4] == "PU" and validators.url(check[1]) and validators.url(check[2]):
	findLinkAndLaunch()

else:
	input("Enter any key to start setup...")
	setup()