formatter = "%r %r %r %r" # 定义变量 formatter

print  formatter % (1,2,3,4) # 代入formatter，就是 print "%r %r %r %r" % (1,2,3,4),字符串后面紧跟变量名
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True) # True 和 False 首字母必须大写，不然报错
print formatter % (formatter,formatter,formatter,formatter)
print formatter % ("I had this thing.",
                   "That you could type up right",
				   "But it did't sing",
				   "So I said goodnight.")

# 数字、变量名、逻辑值不需要加引号

# print formatter % ("一个","两个","三个","四个") 字母

formatter = "%s %s %s %s"
# print formatter % ("一个","两个","三个","四个") 识别的是formatter = "%s %s %s %s",不是第一个formatter，打印还是乱码


