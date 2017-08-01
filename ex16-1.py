from sys import argv   # 从sys 中调取 argv 模块

script, filename = argv # 设置参数给 agrv

print "We're going to erase %r." % filename # 初始化文件
print "If you don't want that, hit CTRL-C(^C)." # 如果不想建立文件，按ctl+c
print "If you do want that, hit RETURN." # 如果想建立文件，按返回，即确定键

raw_input ("?") # 做何选择

print "Opening the file ..." # 打开定义的文件
target = open (filename, 'w')# 定义target，对文件进行写入操作,一定要有‘w’

print "Now I'm going to ask you for three lines." # 写三句话

line1 = raw_input("line1 : ")
line2 = raw_input("line2 : ")
line3 = raw_input("line3 : ")

print "I'm going to write these to the file." # 把三句话写入到文件中

target.write(line1) # 写入第一句话
target.write("\n") # 转行
target.write(line2)# 写入第二句话
target.write("\n") # 转行
target.write(line3) # 写入第三句话
target.write("\n") # 转行

print "Truncating the file. Goodbye!" # 清空文件。这里并没有清空，这条命令放在13行和29行没什么区别
target.truncate() # 清空

print "And finally, we colse it." # 保存文件
target.close() # 保存，这条命令也暂时不知道怎么用

# target 是定义的一个变量，write(), close(), read(), readline(), truncate(),命令的使用都要加上变量名，明确对哪个变量进行操作，对照 ex15-1.py 来看

