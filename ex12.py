age = raw_input("How old are you?")  # raw_input(),括号里面可以直接写提示，加上双引号
height = raw_input("How tall are you ?")
weight = raw_input("How much do you weigh?")

print "So, you're %r old, %r tall, %r heavy." %(
   age, height, weight)
#  %(age, height, weight) 直接这样转行下来不行