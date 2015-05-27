#exercise 1
print("hello world")
print("hello again")
print("i'd much rather you 'not'. \n")
print("------------------------------------\n")

#exercise 2
#this was just about comments

#exercise 3
#the math symbols: + - / * % < > <= >=
print("2/5 is: ", 2 /5)
print("5/2 is: ", 5/2)
print("20.0/5 is: ", 20.0/5)
print("counting chickens: ")
print("hens", 25+30 /6)
print("roosters", 100-25 * 3 %4)

print("is it true that 3 + 2 <5 - 7?")
print (3 + 2 <5 - 7)
print("\n------------------------------------\n")

#exercise 4
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")
print("\n------------------------------------\n")

#exercise 5
my_name = 'Jasmine'
my_age = 21
my_height = 63 # inches
my_weight = 125 # lbs
my_eyes = 'Brown'
my_hair = 'Black'

print ("My name is %s." % my_name)
print ("I am %d inches tall." % my_height)
print ("I have %s eyes and %s hair." % (my_eyes, my_hair))

print ("If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))

print("\n------------------------------------\n")

#exercise 6
x = "there are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)
 
print (x)
print (y)

print("I said: %r" %x) #use %r for debugging, displays raw data
print("I also said: '%s'." %y)
print("\n------------------------------------\n")


#exercise 7
print("mary had a little lamb")
print("its fleece was white as %s" %"snow")
print("and everywhere that mary went")
print("." *10)
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print (end1 + end2 + end3 + end4 + end5 + end6)
print (end7 + end8 + end9 + end10 + end11 + end12)
print("\n------------------------------------\n")

#exercise 8
formatter = "%r %r %r %r"

print (formatter %(1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
	"I had this thing.", 
	"That you could type up right.",
	"But it didn't sing.",
	"So I said good night."
))
print("\n------------------------------------\n")

#exercise 9
print("""
With the three double quotes,
We can print as much as we want
even with tons of lines!!
wow amaze
""")
print("\n------------------------------------\n")

#exercise 10
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

print("\n------------------------------------\n")

