# x is a string with an embedded signed decimal integer (10)
x = "There are %d types of people." % 10
# binary is just a simple string
binary = "binary"
# do_not is just a simple string
do_not = "don't"
# y is a string with the two previous strings also inside it
# %s is string conversion via str() prior to formatting
y = "Those who know %s and those who know %s." % (binary, do_not)

# These lines just print the strings.
print x
print y

# %r is raw string formatting. So that's why it includes the single quotes?
print "I said: %r." % x
# The single quotes are in here manually, since we're not using str()
print "I also said: '%s'." % y

# defining a string
hilarious = False
# embedding a raw string in a string.
joke_evaluation = "Isn't that joke so funny?! %r"

# print the embedded string with the other string as its format variable
print joke_evaluation % hilarious

# defining a string
w = "This is the left side of..."
# defining a string
e = "a string with a right side."

# concatenating the two strings
print w + e
