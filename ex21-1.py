def add(a,b): # 定义一个函数 add,参数为a，b
    print "ADDING %d + %d" % (a,b) # 打印 字符串，利用格式化字符
    return a + b # 返回 a+b的值，将其结果赋予一个变量

def substract(a,b):
    print "SUBSTRACT %d - %d" % (a,b)
    return a - b
	
def multiply(a,b):
    print "MULTIPLY %d * %d" % (a,b)
    return a * b
	
def divide(a,b):
    print "DIVIDE %d / %d" % (a,b)
    return a / b
	
	
print "Let's do some math with just function!" # 打印字符串

age = add(30,5) # 调用函数add，同时将a+b的返回结果赋予变量 age，前面的 return 的功能
height = substract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, iq: %d" %(age,height,weight,iq) # 打印字符串，并利用格式化字符


# A puzzle for the extra credit, type it in anyaway.
print "Here is a puzzle." # 打印字符串

what = add(age,substract(height,multiply(weight,divide(iq,2)))) # 定义变量 what,后面是将函数返回值又当作函数参数。所以实际是 divide(iq,2)  multiply(weight,divide) substract(height,multiply) add(age,substract) 其实是一个类似嵌套计算的函数

print "That becomes:", what, "Can you do it by hand?" # 打印字符串























































