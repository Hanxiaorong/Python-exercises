from sys import argv # 导入sys 模块

script, user_name, age = argv # 设置script, user_name, age 三个参数
prompt = 'Please write your answer \n >' # 设置变量prompt，写出提示语，方便raw_input 直接引用

print "Hi %s, I'm the %s script ." %(user_name, script)
print "I'd like to ask you a few question ."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "How old are you ,is %s ?" % age
ages = raw_input(prompt)

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You are %r years old.
You live in %r, Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, ages, lives, computer)