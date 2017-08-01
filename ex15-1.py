print "Type the filename:" # 下面open要打开的具体文件名，print 要顶格写
filename = raw_input('>')

txt = open(filename) # 返回“file object”
print txt.read() # 读取具体文件的内容
# print txt.readline() 读取文件第一行
# print txt.readlines() 读取文件的所有行
