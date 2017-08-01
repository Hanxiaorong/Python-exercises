people = 30
cars = 30
buses = 15 # 定义三个变量并赋值


if cars > people and cars > buses or people > buses: # 判断布尔表达式的真假，按顺序判断
   print "We should take the cars." # 前面的if 语句为真，则打印这行代码，否则运行下一行
elif cars > people and cars >buses or people > buses: # 判断布尔表达式的真假
   print "We should not take the cars." # elif 虽然也为 true，多个为 true的情况下，只打印第一个
else:
   print "We can't decide."
   
if buses > cars:
   print "That's too many buses."
elif buses < cars:
   print "Mybe we should take the buses."
else: # 判断前面的 if 和 elif,如果都为fales，则打印这行 
   print "We still can't decide."
   
if people > buses:
   print "Alright, let's just take the buses."
else:
   print "Fine, let's stay home then."
