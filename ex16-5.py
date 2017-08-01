filename = raw_input("Write the name of the file:")
target = open(filename, 'w') # 文档写入内容，要加'w'

target.write("hanxiaorong\n  hanxiaorong hanxiaorong\n hanxiaorong hanxiaorong hanxiaorong")
target.write("\n")
target.write("hanxiaorong hanxiaorong")
target.write("\n")
target.write("hanxiaorong hanxiaorong hanxiaorong")


filename = raw_input("Write the name of the file:")
target = open(filename) # 读取文档内容不需要加'w'

print target.read()


