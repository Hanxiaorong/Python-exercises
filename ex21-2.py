def add(a,b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def substract(a,b):
    print "SUBSTRACT %d - %d" % (a,b)
    return a - b
	
def multiply(a,b):
    print "MULTIPLY %d * %d" % (a,b)
    return a * b
	
def divide(a,b):
    print "DIVIDE %d / %d" % (a,b)
    return a / b
	
	
print "Let's do some math with just function!"

age = add(30,5)
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, iq: %d" %(age,height,weight,iq)


# A puzzle for the extra credit, type it in anyaway.
print "Here is a puzzle."

d = divide(iq,2)
m = multiply(weight,d)
s = substract(height,m)
what = add(age,s)

print "That becomes:", what, "Can you do it by hand?"