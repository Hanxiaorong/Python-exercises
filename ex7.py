print "Mary had a little lamb"
print "Its fleece was white as %s." %'snow'
print "And everywhere that Mary went."
print "."*10 # what that do ?

end1 = "c"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#print （end1 + end2 + end3 + end4 + end5 + end6,
#   end7 + end8 + end9 + end10 + end11 + end12） 这样写也不可以

# 为什么在输出字符串的后面加句号就报错，加逗号就不会报错呢？？？？比如 line21 最后end12.就不行，end12,就可以。在 line3 双引号后加,可以，加.不可以。