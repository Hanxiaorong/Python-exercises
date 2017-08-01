def cheese_and_crackers(cheese_count, boxes_of_crackers): # 创建一个带参数的函数，函数名称自定义，一般用字母加下划线组成，按函数的功能命名
    print "You have %d cheese!" % cheese_count # 利用格式化字符给参数赋值
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
	
	
print "We can just give the function numbers directory:"
cheese_and_crackers(20,30)  # 方法一，直接给参数赋值


print "OR, we can use variables from our script:" # 方法二：利用脚本给参数赋值
amount_of_cheese = 10 # 通过定义变量的方式给出参数值
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:" # 方法三： 利用算式的方式给参数赋值
cheese_and_crackers(10+20, 5+6)


print "And we can combine the two, variables and math:" # 方法四：算式与参数的结合使用
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

print "We can use plus the variables from our script:" # 方法五：直接变量相加
cheese_and_crackers(amount_of_cheese+amount_of_cheese, amount_of_crackers+amount_of_crackers)

print "Please tell me the number:"
cheese = raw_input('>')
boxes_of_crackers = raw_input('>')