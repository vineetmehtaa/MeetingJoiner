import webbrowser
import time
from sys   import argv, exit
from os    import system, name
from PDT   import *
from pull  import *
from setup import setup

# function to clear screen
def clear():
  
	# For windows
	if name == 'nt':
		clear = system('cls')
  
	# For mac and linux(here, os.name is 'posix')
	else:
		clear = system('clear')

# function to check and approve meeting launch
def findLinkAndLaunch():
	if time_category == -1 or day == "Sunday":
		input("No Class Right Now!")
		exit()

	else:
		importTT()

# function to import timetable contents
def importTT():
	f = open("details.txt", "r")
	cl = ""
	for i in f:
		cl = i
		break
	f.close()
	cl = cl[5:-1]

	if cl == "PU2 A":
		launch_meeting(ttpuII_A[day][time_category])

	elif cl == "PU2 B":
		launch_meeting(ttpuII_B[day][time_category])

	elif cl == "PU2 C":
		launch_meeting(ttpuII_C[day][time_category])

	elif cl == "PU2 D":
		launch_meeting(ttpuII_D[day][time_category])
	
	elif cl == "PU2 E":
		launch_meeting(ttpuII_E[day][time_category])

	elif cl == "PU2 F":
		launch_meeting(ttpuII_F[day][time_category])

	else:
		print("Your details seem to be wrong, kindly enter [y] to setup the program again, else enter any other key: ")
		ch = input()
		if ch.upper() == "Y":
			setup()
			exit()

# function to launch meeting or inform break
def launch_meeting(link):
	if link == "BREAK":
		input("You have a break right now! Come back later!")
	else:
		webbrowser.get().open(link)
		input("Your meeting should have launched!")
