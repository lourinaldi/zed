print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %s old, %s tall and %s heavy." % (
	age, height, weight)
print "A decade ago you were", age - 10