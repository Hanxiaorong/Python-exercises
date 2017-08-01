the_count = [1, 2, 3, 4, 5]  # 创建一个列表 the_count
fruits = ['apples', 'oranges', 'pears', 'apricots'] # 创建一个列表 fruits
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']# 创建一个列表 change

# this first kind of for-loop goes through a list
for number in the_count:  # numebr 在 the_count中，循环一遍
    print "This is count %d" % number # 按照 the_count 列表的顺序，number 循环一遍

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit # 按照 fruits 列表的顺序，fruit 循环一遍
	
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i
	
# we can also build lists, first start with an empty one
elements = [] # 定义变量 elements

# then use the range function to do 0 to 5 counts
for i in range(0, 7): # 从 0 开始，循环到6停止，最后一个数字不循环
    print "Adding %d to the list." % i # 从 0 开始，递加到第7 个数
	# append is a function that lists understand
    elements.append(i) # 生成 elements 列表
	
# now we can print them out too
for i in elements:
    print "Element was: %d" % i