from sys import argv # 从sys 中导入 agrv 这个模块

script, filename = argv # 设置参数

txt = open (filename) # 返回“ file object”

print "Here's your file %r:" % filename # 返回具体的文件名
print txt.read() # 打印具体文件名的内容

print "Type the filename again:" # 再次打印具体文件名
file_again = raw_input (">") # 输入文件名,这一行删除也能得到同样的结果

txt_again = open(filename) # 返回“ file object”

print txt_again.read() # 打印具体的文件内容