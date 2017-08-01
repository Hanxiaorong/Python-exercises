print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ") # 不加冒号

if door == "1": # 判断 变量door与1 是否相等
   print """There's a giant bear here eating a cheese cake. What do you do?"
            1. Take the cake.
            2. Scream at the bear.
            3. I don't know what to do?"""
   
   bear = raw_input("> ") # 不加冒号
   
   if bear == "1": # 嵌套的if ,也要加冒号，空格
      print "The bear eats your face off. Good job!" # 加空格缩进
   elif bear == "2":
      print "The bear eats your legs off. Good job!"
   else:
      print "Well, doing %s is probably better. Bear runs away." % bear
	  
elif door == "2":
   print """You stare into the endless abyss at Cthulhu's retina."
            1. Bluebarries.
            2. Yellow jacket clothespins.
            3. Understanding revolvers yelling melodies."""
   
   insanity = raw_input("> ")
      
   if insanity == "1" or insanity == "2":
      print "Your body survives powered by a mind of jello. Good job!"
   else:
      print "The insanity rots your eyes into a pool of muck. Good job!"
	  
else:
   print "You stumble around and fell on a knife and die. Good job!"
   
# 对于多个条件判断，多写几个 elif 即可