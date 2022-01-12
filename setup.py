from os  import system, name
from sys import argv, exit
import validators
import string

def clear():
  
	# For windows
	if name == 'nt':
		clear = system('cls')
  
	# For mac and linux(here, os.name is 'posix')
	else:
		clear = system('clear')

def setup():
	f = open('details.txt', 'r+')
	f.truncate(0) # need '0' when using r+
	f.close()

	f = open("details.txt", "r")
	if f.read() == "":
		clear()
		print("Hey! Welcome to the setup!\n")
		print("What is your Stream?")
		print("\n1. Science")
		print("2. Commerce\n")
		a = input("Enter the number [1 / 2]: ")
		if a != "1" and a != "2":
			print("Sorry! Try Again!")
			exit()

		else:
			clear()
			if a == "1":
				a = "PCM"
				print("\nEnter your optional subject: ")
				print("\n1. Biology")
				print("2. Computer Science\n")
				b = input("Enter the number [1 / 2]: ")
				
				if b != "1" and b != "2":
					print("Sorry! Try Again!")
					exit()

				else:
					if b == "1":
						b = "B"
					else:
						b = "C"

			else:
				a = "EAB"
				print("\nEnter your optional subject: ")
				print("\n1. Statistics")
				print("2. Computer Science\n")
				b = input("Enter the number [1 / 2]: ")
				if b != "1" and b != "2":
					print("Sorry! Try Again!")
					exit()
				else:
					if b == 1:
						b = "S"
					else:
						b = "C"

		clear()
		print("\nWhat is your grade?")
		print("\n1. PU - I")
		print("2. PU - II\n")
		c = input("Enter the number [1 / 2]: ")

		if c != "1" and c!= "2":
			print("Sorry! Try Again!")
			exit()

		else:
			if c == "1":
				c = "PU1"
			else:
				c = "PU2"

		clear()
		d = input("\nWhich section are you in? ")
		if "dDeEfFgG".find(d) == -1:
			print("Sorry! Try Again!")
			exit()

		clear()

		print("\nMake sure you enter the link starting with http or https!")
		optional = input("\nEnter the link for your optional subject [Biology / CS / Statistics]: ")
		if optional.startswith("http") == False and optional.startswith("HTTP") == False:
			clear()
			print("Invalid link entered! You will have to start over.")
			exit()
		else:
			if not validators.url(optional):
				clear()
				print("Invalid link entered! You will have to start over.")
				exit()

		clear()

		print("\nMake sure you enter the link starting with http or https!")
		language = input("\nEnter the link for your language subject [Hindi / Kannada / French]: ")
		if language.startswith("http") == False and language.startswith("HTTP") == False:
			clear()
			print("\nInvalid link entered! You will have to start over.")
			exit()
		else:
			if not validators.url(language):
				clear()
				print("\nInvalid link entered! You will have to start over.")
				exit()

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

		combination = (a + b + " " + c + " "+ d).upper()
		file1 = open("details.txt", "w")
		file1.write(combination + "\n" + optional + "\n" + language)
		file1.close()

		clear()
		print("\nGreat! Looks like you're all good!")
		input("Your auto meeting joiner is now ready for use!\nYou may run the program again to join your classes!")
		exit()