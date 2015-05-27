#exercise 16

from sys import argv

script, filename = argv

print ("we're going to erase %r." % filename)
print("if you don't want that, hit ctrl-c")
print("if you do, hit return")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Deleting the file contents...")
target.truncate()

print("Now I'm going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("Writing to file...")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.close()