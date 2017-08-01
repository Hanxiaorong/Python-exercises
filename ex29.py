people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!" # 空格不一定是4个，但是4个更美观
	
if people > cats:
    print "Not many cats! The world is saved!"
	
if people < dogs:
    print "The world is drooled on!"
	
if people > dogs:
    print "The world is dry!"
	
	
dogs += 5 # 递增运算，相当于 dogs = dogs + 5

if people >= dogs:
    print "People are greater than or equal to dogs."
	
if people <= dogs:
    print "People are less than or equal to dogs."
	
	
if people == dogs:
    print "People are dogs."