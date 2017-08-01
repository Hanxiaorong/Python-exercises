people = raw_input("people = ")
cats = raw_input("cats = ")
dogs = int(raw_input("dogs = ")) # 不知道为什么只输出 people >= dogs, 后面两个带等号的未输出

# people = 25
# cats = 15
# dogs = 20

if people < cats:
    print "Too many cats! The world is doomed!"
	
if people > cats:
    print "Not many cats! The world is saved!"
	
if people < dogs:
    print "The world is drooled on!"
	
if people > dogs:
    print "The world is dry!"
	

	
	
dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."
	
if people <= dogs:
    print "People are less than or equal to dogs."
	
	
if people == dogs:
    print "People are dogs."