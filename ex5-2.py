name = 'Zed A. Shaw'
age = 35 # not a line 
height = 74 # inches 
weight = 180 # labs
eyes = 'Blue'
teeth = 'White'
hair = 'Broen'

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %r hair." % (eyes, hair)
print "His teeth are usually %r depending on the coffee."% teeth

# this line is tricky, try to get it exactly right
print "If I add %rr, %rr, and %rr I get %rr." %(
    age, height, weight, age + height + weight)
	
# 把my_去掉后，只要定义的变量和后面的对应起来，就可以输出。
# %s、%d、r% 是一种格式控制工具，格式化字符是有特定的，比如 q% 就不行
# 格式化字符不能是两个以上的字母，只能是一个，比如 %rr 就会输出一个r
# %%	百分号标记 #就是输出一个%
# %c	字符及其ASCII码
# %s	字符串
# %d	有符号整数(十进制)
# %u	无符号整数(十进制)
# %o	无符号整数(八进制)
# %x	无符号整数(十六进制)
# %X	无符号整数(十六进制大写字符)
# %e	浮点数字(科学计数法)
# %E	浮点数字(科学计数法，用E代替e)
# %f	浮点数字(用小数点符号)
# %g	浮点数字(根据值的大小采用%e或%f)
# %G	浮点数字(类似于%g)
# %p	指针(用十六进制打印值的内存地址)
# %n	存储输出字符的数量放进参数列表的下一个变量中
# %r    用来做调式最好，可以打印任何变量
# 格式化字符是一个重难点，后面要多学习