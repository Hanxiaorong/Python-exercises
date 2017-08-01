# Here's some new strange stuff , remember type it exactly.

days = "Mon Tue Wen Thu Fri Sat Sun"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" # \n 是换行的意思

print "Here are the days:",days
print "Here are the months:",months

print """
There's something going on here.
With the double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want,or 5,or 6.
""" # 三个引号必须连着，中间不能有空格，否则报错


print "Here are the months '%r'." % months  # 这里不能用%r ，否则\n 分行不起作用