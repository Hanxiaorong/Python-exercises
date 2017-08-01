x = "There are %d type of people." % 10  # 定义一个变量，变量中包含格式化字符
binary = "binary" # 定义的变量可以是个文本，双引号里面的内容就是文本
do_not = "don't"  # 同上
y = "Those who know %s and those who %s ." %(binary,do_not) # 定义的变量中包含多个格式化变量，字符串后面紧跟格式化的变量，binary对应第一个格式化变量，do_not对应第二个格式化变量。注意要用（），括号里面用逗号隔开。

print x # 输出定义的变量x
print y # 输出定义的变量y

print "I said: %r." %x  # 输出一个字符串，字符串中包含格式化的变量
print "I also said: '%s'." %y # 同上

hilarious = False # 定义变量hilarious
joke_evaluation = "Isn't that joke so funny?! %r"  # 定义一个变量，%r是格式化变量，对应输出中的%hilarious

print joke_evaluation % hilarious # 输出变量joke_evaluation,"Isn't that joke so funny?! %r" %hilarious 这样看更明白点。这里犯了个错误，joke的j写成大写，报错，所以定义变量与输出的要完全一致，包括单词的大小写

w = "This is the left side of ..."
e = "a string with a right side."

print w + e # 两个字符串也可以相加，然后打印出来。

# a = "There is a lot of people,include American ,chinese,Japean and so on."
# b = "include American ,chinese,Japean and so on."
# print a - b  报错，目前看来只能是 + 
