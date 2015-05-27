#exercise 18: functions

#this one is like the scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print ("arg1: %r, arg2: %r" % (arg1, arg2))

#the *args is pointless
def print_two_again(arg1, arg2):
	print("arg1: %r, arg2: %r" % (arg1, arg2))

#this takes one argument
def print_one(arg1):
	print ("arg1: %r" % arg1)

#this takes no arguments
def print_none():
	print ("no arguments")

print_two("jasmine", "nike")
print_two_again("jasine" , "nike")
print_one("hi!!!")
print_none()