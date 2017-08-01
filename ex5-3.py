inches = 2.54 # cm
pounds = 0.454 # kg

height = 74.0 # inches 
weight = 180.0 # labs

cm = height*inches
kg = weight*pounds

print cm
print kg

print "He's %d cm tall." % cm # 没有小数是因为%d 有符号整数
print "He's %d kg heavy." % kg

#换成 %e 结果就有小数
print "He's %f cm tall." % cm # 因为%f 带小数点
print "He's %f kg heavy." % kg

print "He's %g cm tall." % cm 
print "He's %g kg heavy." % kg

# 带小数直接选择 %g 