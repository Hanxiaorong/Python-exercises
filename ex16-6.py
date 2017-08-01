filename = raw_input("Write the name of the file:")
target = open(filename, 'w') # 清空文档内容，要加'w'

target.truncate()
