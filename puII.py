"""
##### Subjects #####
SUB1 = OPTIONAL
SUB2 = LANGUAGE
SUB3 = ENG
SUB4 = ACC / PHY
SUB5 = ECO / CHE
SUB6 = BST / MAT
"""

"""
classFormat = [
	"www.sub3.com", # ENGLISH
	"www.sub4.com", # ACC or PHY
	"www.sub5.com", # ECO or CHE
	"www.sub6.com"	# BST or MAT
]
"""

sublist = []
f = open("details.txt", "r")
x = f.readlines()
f.close()

class2D = [
	"https://meet.google.com/nqu-onem-oya",
	"https://meet.google.com/tvp-qhfc-yvk",
	"meet.google.com/vgm-ymnq-ukz",
	"https://zoom.us/j/92340729929?pwd=NS9aTUk3dm5YVVpMMm56WjdKT1pMQT09"
]

class2E = [
	"https://meet.google.com/nqu-onem-oya",
	"https://meet.google.com/tvp-qhfc-yvk",
	"https://zoom.us/j/92516506148?pwd=ZWlyaUlRcGZseVF6QkY5WGh6UCtPZz09",
	"https://zoom.us/j/92340729929?pwd=NS9aTUk3dm5YVVpMMm56WjdKT1pMQT09"
]

class2F = [
	"https://zoom.us/j/6438898336?pwd=ejQ4OWRMMllMZHpYdkRuL21LYUxtZz09",
	"https://meet.google.com/tvp-qhfc-yvk",
	"https://zoom.us/j/92516506148?pwd=ZWlyaUlRcGZseVF6QkY5WGh6UCtPZz09",
	"https://zoom.us/j/92340729929?pwd=NS9aTUk3dm5YVVpMMm56WjdKT1pMQT09"
]

sublist.append(x[1][:-1])
sublist.append(x[2])
section = (x[0][:-1])[-1]

if section == "D":
	for i in class2D:
		sublist.append(i)

if section == "E":
	for i in class2E:
		sublist.append(i)

if section == "F":
	for i in class2F:
		sublist.append(i)

SUB1 = sublist[0]
SUB2 = sublist[1]
SUB3 = sublist[2]
SUB4 = sublist[3]
SUB5 = sublist[4]
SUB6 = sublist[5]

ttpuII_D = {
	"Monday"	: [SUB4, SUB5, SUB1, "BREAK", SUB3, SUB6],
	"Tuesday"	: [SUB1, SUB4, SUB5, "BREAK", SUB6, SUB6],
	"Wednesday" : [SUB5, SUB6, SUB4, "BREAK", SUB1, SUB1],
	"Thursday"	: [SUB1, SUB2, SUB6, "BREAK", SUB5, SUB4],
	"Friday"	: [SUB3, SUB4, SUB2, "BREAK", SUB1, SUB5],
	"Saturday"	: [SUB5, "BREAK", SUB1, "BREAK", SUB6, SUB4]
}

ttpuII_E = {
	"Monday"  	: [SUB1, SUB5, SUB4, "BREAK", SUB6, SUB3],
	"Tuesday" 	: [SUB5, SUB1, SUB4, "BREAK", SUB1, SUB1],
	"Wednesday" : [SUB4, SUB1, SUB5, "BREAK", SUB6, SUB6],
	"Thursday" 	: [SUB2, SUB4, SUB5, "BREAK", SUB6, SUB1],
	"Friday" 	: [SUB2, SUB6, SUB5, "BREAK", SUB4, SUB3],
	"Saturday" 	: [SUB1, SUB4, "BREAK", "BREAK", SUB5, SUB6]
}

ttpuII_F = {
	"Monday"	: [SUB1, SUB3, SUB6, "BREAK", SUB5, SUB4],
	"Tuesday"	: [SUB4, SUB1, SUB5, "BREAK", SUB1, SUB1],
	"Wednesday" : [SUB6, SUB1, SUB3, "BREAK", SUB4, SUB5],
	"Thursday"	: [SUB5, SUB6, SUB4, "BREAK", SUB2, SUB1],
	"Friday"	: [SUB6, SUB2, SUB6, "BREAK", SUB5, SUB4],
	"Saturday"	: [SUB1, SUB5, SUB6, "BREAK", SUB4, "BREAK"]
}

# ttpuII_F = {
	# "Monday"	: [SUB, SUB, SUB, "BREAK", SUB, SUB],
	# "Tuesday"	: [SUB, SUB, SUB, "BREAK", SUB, SUB],
	# "Wednesday" : [SUB, SUB, SUB, "BREAK", SUB, SUB],
	# "Thursday"	: [SUB, SUB, SUB, "BREAK", SUB, SUB],
	# "Friday"	: [SUB, SUB, SUB, "BREAK", SUB, SUB],
	# "Saturday"	: [SUB, SUB, SUB, "BREAK", SUB, SUB]
# }
