def cheese_and_crackers(cheese_count, boxes_of_crackers): 
   print "You have %d cheese!" % cheese_count
   print "You have %d boxes of crackers!" % boxes_of_crackers
   print "Man that's enough for a party!"
   print "Get a blanket.\n"
	
print "Please tell me the number:"
numb1 = int(raw_input('>'))
numb2 = int(raw_input('>'))

cheese_and_crackers(int(numb1), numb2)

print "Let's change an other way:"
print "Please tell me the number:"
numb1 = raw_input('>')
numb2 = raw_input('>')

cheese_and_crackers(int(numb1), int(numb2))