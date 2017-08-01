from sys import argv  # 调用模块argv

script, input_file = argv # 设置两个变量

def print_all(f): # 定义一个带参数的函数 print_all(f), 参数为f
    print f.read() # 读取函数参数 f

def rewind(f): # 定义一个带参数的函数 rewind(f), 参数为f
    f.seek(0)  # 返回参数的字节
	
def print_a_line(line_count, f): # 定义一个带参数的函数 print_a_line, 参数为 line_count, f
    print line_count, f.readline() # 读取函数参数 line_count, f.
	
current_file = open(input_file) # 定义变量 current_file, 打开文件 input_file

print "First let's print the whole file:\n" # 打印字符串

print_all(current_file) # 给函数 print_all 的参数赋值，实质是调用函数

print "Now let's rewind, kind of like a tape." # 打印字符串

rewind(current_file) # 给函数 rewind 的参数赋值，也就是调用函数

print "Let's print three lines:" # 打印字符串

current_line = 1 # 定义变量current_line
print_a_line(current_line, current_file) # 给函数 print_a_line 的参数赋值，调用函数

current_line = current_line + 1 # 定义变量 current_line，current_line 变量的传递
print_a_line(current_line, current_file) # 给函数 print_a_line 的参数赋值，调用函数

current_line = current_line + 1 # 定义变量 current_line，在上一个 currrent 上加1
print_a_line(current_line, current_file) # 给函数 print_a_line 的参数赋值，调用函数

# 另外，在12行 print 这里结尾加逗号，看看结果有什么不一样。
# 当对一个程序不懂时，就几行几行慢慢运行，通过运行结果一点点去理解


