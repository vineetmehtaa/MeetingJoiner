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
		input("Time of execution: " + time.ctime())
		
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
	
	elif link == "PT":
		print_timetable(ct, section, "P")
	
	elif link == "LAB":
		print_timetable(ct, section, "L")

	else:
		print_timetable(ct, section, "C")
		webbrowser.get().open(link)

# function to print timetable
def print_timetable(ct, section, status):
	sub_called = ""
	todays_schedule = []

	for i in ct:
		if i != day:
			continue

		for j in ct[i]:
			if "ABC".find(section) != -1:
				if j == SUB1:
					todays_schedule.append("OPT")
				
				elif j == SUB2:
					todays_schedule.append("LANG")
				
				elif j == SUB3:
					todays_schedule.append("ENG")

				elif j == SUB4:
					todays_schedule.append("PHY")

				elif j == SUB5:
					todays_schedule.append("CHE")

				elif j == SUB6:
					todays_schedule.append("MATH")

				elif j == "BREAK":
					todays_schedule.append("BREAK")
				
				elif j == "LAB":
					todays_schedule.append("LAB")

				else:
					todays_schedule.append("PT")
			
			else:
				if j == SUB1:
					todays_schedule.append("OPT")
				
				elif j == SUB2:
					todays_schedule.append("LANG")
				
				elif j == SUB3:
					todays_schedule.append("ENG")

				elif j == SUB4:
					if section != "D":
						todays_schedule.append("ACC")
					else:
						todays_schedule.append("AC/BS")

				elif j == SUB5:
					todays_schedule.append("ECO")

				elif j == SUB6:
					todays_schedule.append("BST")
				
				elif j == "BREAK":
					todays_schedule.append("BREAK")
				
				else:
					todays_schedule.append("PT")

	clear()
	f = open("details.txt", "r")
	cbl = f.readlines()
	combination = cbl[0][5:8]
	f.close()

	print("\n------------------------")
	print("    TODAY'S SCHEDULE")
	print("------------------------")
	print("       " + cbl[0][:-1])

	if day == "Wednesday" or day == "Thursday":
		print("        " + day.upper())

	else:
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

	runt = 6
	if len(ct[day]) == 7:
		time_list.append(" 1:00 -  2:50 ---> ")
		runt = 7

	sublist = []
	for i in range(0, runt):
		print(time_list[i] + todays_schedule[i])
		sublist.append(ct[day][i])
	
	print("------------------------")
	print("      TIME - " + str(now.strftime("%H:%M")))

	if status == "C":
		print("      SUB  - " + todays_schedule[i])
		print("------------------------")
		for i in range(1,10):
			print("    LAUNCHING IN " + str(10-i) + "s", end="\r")
			time.sleep(1)
		print("    MEETING LAUNCHED")
		print("------------------------")

	elif status == "P":
		print("       SUB - PT")
		print("------------------------")
		print("     YOU HAVE PT NOW")
		print("------------------------")

	elif status == "L":
		print("       SUB - LAB")
		print("------------------------")
		print("  KINDLY USE YOUR OWN")
		print(" LINK FOR CORE SUB LAB")
		print("------------------------")

	else:
		print("       SUB - BREAK")
		print("------------------------")
		print("    YOU HAVE A BREAK")
		print("------------------------")