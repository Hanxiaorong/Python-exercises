i = 0
numbers = []

while i < 6:
    print "At the top i is %d" %i # i 值为一开始定义的 0
    numbers.append(i) # 把 i 的值放到列表 numbers 中去

    i = i+1 # 这行命令是针对10 行起作用的，与9行无关
    print "Numbers now: ", numbers # 逗号（,）不能省，打印列表
    print "At the bottom i is %d" %i # i 取一个新值，开始新一轮的循环
    
   
	
	
print "The numbers: "

for num in numbers:
    print num # 打印列表中的值