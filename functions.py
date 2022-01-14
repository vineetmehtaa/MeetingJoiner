import webbrowser
import time
from sys    import argv, exit
from os     import system, name
from PDT    import *
from pull   import *
from setup  import setup

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
		clear()
		print("No class right now!")
		print("Time : " + str(t).replace(".", ":"))
		print("Day  : " + day)
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
		launch_meeting(ttpuI_A[day][time_category], ttpuI_A, cl[-1])

	elif cl == "PU1 B":
		launch_meeting(ttpuI_B[day][time_category], ttpuI_B, cl[-1])

	elif cl == "PU1 C":
		launch_meeting(ttpuI_C[day][time_category], ttpuI_C, cl[-1])

	elif cl == "PU1 D":
		launch_meeting(ttpuI_D[day][time_category], ttpuI_D, cl[-1])
	
	elif cl == "PU1 E":
		launch_meeting(ttpuI_E[day][time_category], ttpuI_E, cl[-1])

	elif cl == "PU1 F":
		launch_meeting(ttpuI_F[day][time_category], ttpuI_F, cl[-1])

	# PU - II
	elif cl == "PU2 A":
		launch_meeting(ttpuII_A[day][time_category], ttpuII_A, cl[-1])

	elif cl == "PU2 B":
		launch_meeting(ttpuII_B[day][time_category], ttpuII_B, cl[-1])

	elif cl == "PU2 C":
		launch_meeting(ttpuII_C[day][time_category], ttpuII_C, cl[-1])

	elif cl == "PU2 D":
		launch_meeting(ttpuII_D[day][time_category], ttpuII_D, cl[-1])
	
	elif cl == "PU2 E":
		launch_meeting(ttpuII_E[day][time_category], ttpuII_E, cl[-1])

	elif cl == "PU2 F":
		launch_meeting(ttpuII_F[day][time_category], ttpuII_F, cl[-1])

	# Incase there's an error, user is sent to setup if necessary
	else:
		print("Your details seem to be wrong, kindly enter [y] to setup the program again, else enter any other key: ")
		ch = input()
		if ch.upper() == "Y":
			setup()
			exit()

# function to launch meeting or inform break
def launch_meeting(link, ct, section):
	if link == "BREAK":
		print_timetable(ct, section, "B")

	else:
		print_timetable(ct, section, "C")
		webbrowser.get().open(link)

# function to print timetable
def print_timetable(ct, section, status):
	sub_called = ""

	for i in ct:
		count = 0
		for j in ct[i]:
			if "ABC".find(section) != -1:
				if j == SUB1:
					ct[i][count] = ("OPT")
				
				elif j == SUB2:
					ct[i][count] = ("LANG")
				
				elif j == SUB3:
					ct[i][count] = ("ENG")

				elif j == SUB4:
					ct[i][count] = ("PHY")

				elif j == SUB5:
					ct[i][count] = ("CHE")

				elif j == SUB6:
					ct[i][count] = ("MATH")

				count += 1
			
			else:
				if j == SUB1:
					ct[i][count] = ("OPT")
				
				elif j == SUB2:
					ct[i][count] = ("LANG")
				
				elif j == SUB3:
					ct[i][count] = ("ENG")

				elif j == SUB4:
					ct[i][count] = ("ACC")

				elif j == SUB5:
					ct[i][count] = ("ECO")

				elif j == SUB6:
					ct[i][count] = ("BST")

				count += 1

	clear()
	f = open("details.txt", "r")
	cbl = f.readlines()
	combination = cbl[0][5:8]
	f.close()

	print("\n------------------------")
	print("    TODAY'S SCHEDULE")
	print("------------------------")
	print("       " + cbl[0][:-1])
	print("         " + day.upper())
	print("------------------------")
	time_list = []

	if combination == "PU1":
		time_list.append(" 8:10 -  9:10 ---> ")
		time_list.append(" 9:10 - 10:00 ---> ")
		time_list.append("10:00 - 10:10 ---> ")
		time_list.append("10:10 - 11:00 ---> ")
		time_list.append("11:00 - 11:50 ---> ")
		time_list.append("11:50 - 12:40 ---> ")
	
	else:
		time_list.append(" 8:10 -  9:10 ---> ")
		time_list.append(" 9:10 - 10:00 ---> ")
		time_list.append("10:00 - 10:50 ---> ")
		time_list.append("10:50 - 11:00 ---> ")
		time_list.append("11:00 - 11:50 ---> ")
		time_list.append("11:50 - 12:40 ---> ")

	sublist = []
	for i in range(0, 6):
		print(time_list[i] + ct[day][i])
		sublist.append(ct[day][i])

	print("------------------------")
	print("      TIME - " + str(now.strftime("%H:%M")))
	if status == "C":
		print("      SUB  - " + sublist[time_category])
		print("------------------------")
		for i in range(0,5):
			print("    LAUNCHING IN " + str(5-i) + "s", end="\r")
			time.sleep(1)
		print("    MEETING LAUNCHED")
		print("------------------------")

	else:
		print("      SUB  - BREAK")
		print("------------------------")
		print("    YOU HAVE A BREAK")
		print("------------------------")