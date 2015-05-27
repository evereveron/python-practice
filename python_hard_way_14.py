from sys import argv

#exercise 14
# one command line argument
script, user_name = argv
prompt = '> '

print ("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s" %user_name)
likes = input(prompt)

print("where do you live?")
lives = input(prompt)

print("""
So you said %r about liking me.
You live in %r.
""" % (likes, lives))