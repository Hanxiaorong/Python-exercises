from sys import argv

script, user_name = argv
prompt = 'Please write your answer \n >' # 更换提示语，输出的时候进行转行p'y

print "Hi %s, I'm the %s script ." %(user_name, script)
print "I'd like to ask you a few question ."
print "Do you like me %s ?" % user_name
likes = raw_input(prompt)

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)