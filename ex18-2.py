# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" %(arg1,arg2)  # 在ex18.py 中报错，是因为print 前面不是4个空格，一定要空格键敲入。
	
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %(arg1,arg2)
	
# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1
	
# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("A1877","Shaw")  
print_two_again("A1877","Shaw")
print_one("First!")
print_none()	

# IndentationError: unexpected indent 错误是指tab和空格混用了