my_name = 'Zed A. Shaw'  # 定义一个变量 my_name
my_age = 35 # not a line  定义一个变量 my_age
my_height = 74 # inches 
my_weight = 180 # labs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Broen'

print "Let's talk about %s." % my_name  # 在""里面，也就是字符串插入变量，%s是定义的变量，引号外面的是之前的定义
print "He's %d inches tall." % my_height # 理由同上
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee."% my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(
    my_age, my_height, my_weight, my_age + my_height + my_weight)
	
# 总结：双引号里面定义了插入了多少个变量，引号外面进行一一对应即可。
# 有多个变量时，记得用（）括起来。
