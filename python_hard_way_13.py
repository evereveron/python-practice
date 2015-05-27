from sys import argv
#exercise 13

#run like so:
	# python python_hard_way_13.py first 2nd 3rd
	# as long as there are 3 arguments!
	# the filename is the first one
script, first, second, third = argv

print ("The script is called:", script)
print ("Your first variable is:", first)
print ("Your second variable is:", second)
print ("Your third variable is:", third)
print("\n------------------------------------\n")