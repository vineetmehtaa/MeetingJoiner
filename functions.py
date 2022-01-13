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

	# PU - I
	if cl == "PU1 A":
		launch_meeting(ttpuI_A[day][time_category], ttpuI_A)

	elif cl == "PU1 B":
		launch_meeting(ttpuI_B[day][time_category], ttpuI_B)

	elif cl == "PU1 C":
		launch_meeting(ttpuI_C[day][time_category], ttpuI_C)

	elif cl == "PU1 D":
		launch_meeting(ttpuI_D[day][time_category], ttpuI_D)
	
	elif cl == "PU1 E":
		launch_meeting(ttpuI_E[day][time_category], ttpuI_E)

	elif cl == "PU1 F":
		launch_meeting(ttpuI_F[day][time_category], ttpuI_F)

	# PU - II
	elif cl == "PU2 A":
		launch_meeting(ttpuII_A[day][time_category], ttpuII_A)

	elif cl == "PU2 B":
		launch_meeting(ttpuII_B[day][time_category], ttpuII_B)

	elif cl == "PU2 C":
		launch_meeting(ttpuII_C[day][time_category], ttpuII_C)

	elif cl == "PU2 D":
		launch_meeting(ttpuII_D[day][time_category], ttpuII_D)
	
	elif cl == "PU2 E":
		launch_meeting(ttpuII_E[day][time_category], ttpuII_E)

	elif cl == "PU2 F":
		launch_meeting(ttpuII_F[day][time_category], ttpuII_F)

	# Incase there's an error, user is sent to setup if necessary
	else:
		print("Your details seem to be wrong, kindly enter [y] to setup the program again, else enter any other key: ")
		ch = input()
		if ch.upper() == "Y":
			setup()
			exit()

# function to launch meeting or inform break
def launch_meeting(link, ct):
	if link == "BREAK":
		input("You have a break right now! Come back later!")
	else:
		print(ct)
		webbrowser.get().open(link)
		input("Your meeting should have launched!")