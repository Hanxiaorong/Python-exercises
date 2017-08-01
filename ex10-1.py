tablly_cat = "\t I'm tabbed in."  # \t 是一个转义序列，表示空格的意思，相当于（tab)
persian_cat = "I'm split \n on a line." # \n 表示换行
backslash_cat = "I'm \\ a \\ cat." # \\  转义序列中，双\\打印出单\

fat_cat = """
I'll do a list :
\t * Cat food
\t * Fishies
\t * Catnip\n\t * Grass
""" # """ 也是一个转义序列，表示可以输入多个字符串，注意*号与单词之间的空格，有空格就会打印，没有就不打印

print tablly_cat
print persian_cat
print backslash_cat
print fat_cat

# 使用了转义序列，空格也会被打印出来