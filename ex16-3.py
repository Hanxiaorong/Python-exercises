from sys import argv

script, filename = argv
target = open(filename)

print target.read()

filename = raw_input('>')
txt = open(filename) # 这里的txt 可以换成target，这样的话就要输入 abc.txt才能读取，不用target，则可以输入相应的文档名进行读取

print  txt.read()

# 打开文件的两种方式
