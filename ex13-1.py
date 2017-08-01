from sys import argv  # 把sys模块导入

script, first, second, third, fourth, fifth = argv # 不能用1，2，3，4，5来代替，识别不出来
print "There is a scirpt:",script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
print "Your fifth variable is:", fifth

# 运行打印的时候是参数赋值给变量的过程，可赋值成1，2，3，4，5，>python ex13-1.py 1 2 3 4 5

