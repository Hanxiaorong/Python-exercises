def break_words(stuff):
    """This function will break up words for us.""" # 不一定是4个空格，但是下面的都要对齐，并且有空格
    words = "%r +%r +%r" %(1,2,3) # 这里定义的变量不能赋值给函数参数
    return words
	
sentence = 456 # 为什么定义的变量 sentence 的值对打印函数没有影响？ 

print break_words(sentence) # 引用函数必须给参数赋值，所以定义一个变量 sentence


def break_words(stuff):
    """This function will break up words for us."""
    words = "%r +%r +%r" %(1,2,3) 
    return words

print break_words(456) # 有可能是定义的函数中有return，所以无论函数参数赋任何值，最终都是返回定义的函数值


def break_words(stuff):
    """This function will break up words for us."""
    words = "%r +%r +%r" %(1,2,3) 
    return words

sentence = 456
words = break_words(sentence)
print break_words(words)



def add(a,b):
    return a + b  # 定义的函数，返回值为 a+b
	
age = add(30,5)
height = 20
print add(age,height)



def break_words(stuff):
    """This function will break up words for us."""
    words = "%r +%r +%r" %(1,2,3)
    print words
	
sentence = 456

print break_words(sentence) # 为什么这里返回的值是空值呢？

# def 是定义一个函数，下面有4个空格的都属于这个函数内，可以理解成一个一个的条件，因此函数内定义的变量不能赋值给函数。函数定义完后，接下来要顶格写，引用函数时需要给函数参数赋值，用到变量时，需要重新定义一个变量。