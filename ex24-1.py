print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intution
and requires an explanation
\n\t\twhere there is none.
""" # 转义序列可以连续使用

print "---------------"
print poem
print "---------------"


five = 10 - 2 + 3 - 6 # 定义变量 five ,式子会直接计算
print "This should be five: %s" % five

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    #add = jelly_beans + jars + crates
    return jelly_beans, jars, crates # def 括起来的是一个整体，表示建立一个函数，给出三个相应的条件，最后返回三个值,给四个条件就返回四个值
	
	
start_point = 10000 # 定义变量 start_point
beans, jars, crates = secret_formula(start_point) # 将函数返回的值赋给三个变量，变量名任意

print secret_formula(start_point) # 查看函数的结果，返回三个值

print "With a starting point of: %d" %start_point 
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)