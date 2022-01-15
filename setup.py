from os  import system, name
from sys import argv, exit
import validators
import string

# function to clear screen
def clear():
  
	# For windows
	if name == 'nt':
		clear = system('cls')
  
	# For mac and linux(here, os.name is 'posix')
	else:
		clear = system('clear')
		
# function to instantiate setup for "details.txt"
def setup():
	# clearing "details.txt" incase any information is there that could cause tampering
	f = open('details.txt', 'r+')
	f.truncate(0)
	f.close()
	
	# taking essential details
	f = open("details.txt", "r")
	if f.read() == "":

		# input for stream
		clear()
		print("Hey! Welcome to the setup!\n")
		print("What is your Stream?")
		print("\n1. Science")
		print("2. Commerce\n")
		a = input("Enter the number [1 / 2]: ")

		# validating input
		if a != "1" and a != "2":
			print("Sorry! Try Again!")
			exit()

		else:
			# input for optional subject in Science Stream
			clear()
			if a == "1":
				a = "PCM"
				print("\nEnter your optional subject: ")
				print("\n1. Biology")
				print("2. Computer Science\n")
				b = input("Enter the number [1 / 2]: ")
				
				# validating input
				if b != "1" and b != "2":
					print("Sorry! Try Again!")
					exit()

				else:
					if b == "1":
						b = "B"
					else:
						b = "C"

			else:
				# input for optional subject in Commerce Stream
				a = "EAB"
				print("\nEnter your optional subject: ")
				print("\n1. Statistics")
				print("2. Computer Science\n")
				b = input("Enter the number [1 / 2]: ")

				# validating input
				if b != "1" and b != "2":
					print("Sorry! Try Again!")
					exit()

				else:
					if b == "1":
						b = "S"
					else:
						b = "C"

		# input for grade
		clear()
		print("\nWhat is your grade?")
		print("\n1. PU - I")
		print("2. PU - II\n")
		c = input("Enter the number [1 / 2]: ")

		# validating input
		if c != "1" and c!= "2":
			print("Sorry! Try Again!")
			exit()

		else:
			if c == "1":
				c = "PU1"
			else:
				c = "PU2"

		# input for student section
		clear()
		d = input("\nWhich section are you in? ")
		if "aAbBcCdDeEfF".find(d) == -1:
			print("Sorry! Try Again!")
			exit()

		# taking input for optional subject link
		clear()
		print("\nMake sure you enter the link starting with http or https!")
		optional = input("\nEnter the link for your optional subject [Biology / CS / Statistics]: ")
		
		# validating the optional subject link
		if optional.startswith("http") == False and optional.startswith("HTTP") == False:
			clear()
			print("Invalid link entered! You will have to start over.")
			exit()
		else:
			if not validators.url(optional):
				clear()
				print("Invalid link entered! You will have to start over.")
				exit()
		
		# taking input for language subject link
		clear()
		print("\nMake sure you enter the link starting with http or https!")
		language = input("\nEnter the link for your language subject [Hindi / Kannada / French]: ")
		
		# validating the optional subject link
		if language.startswith("http") == False and language.startswith("HTTP") == False:
			clear()
			print("\nInvalid link entered! You will have to start over.")
			exit()
		else:
			if not validators.url(language):
				clear()
				print("\nInvalid link entered! You will have to start over.")
				exit()
		
		# displaying details to the user to confirm their information
		clear()
		print("############### Profile Details ###############")
		print("\nCombination : " + a+b)
		print("Class       : " + c)
		print("Section     : " + d.upper())
		print("\nOptional subject Meeting link : " + optional)
		print("Language Meeting Link         : " + language)
		choice = ""
		choice = input("\nAre these details correct?[y/n] ")

		if "yY".find(choice) == -1:
			print("You are required to fill the details again!\nKindly relaunch the application!")
			exit()
		
		# preparing information and writing it to "details.txt"
		combination = (a + b + " " + c + " "+ d).upper()
		file1 = open("details.txt", "w")
		file1.write(combination + "\n" + optional + "\n" + language)
		file1.close()

		clear()
		print("\nGreat! Looks like you're all good!")
		input("Your auto meeting joiner is now ready for use!\nYou may run the program again to join your classes!")
		exit()
