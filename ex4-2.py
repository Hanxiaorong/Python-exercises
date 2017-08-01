cars = 100 #定义cars = 100
space_in_a_car = 4 #把4.0改成4，看看结果
drivers = 30 # 定义drivers
passengers = 90
cars_not_driven = cars - drivers # 根据上面的定义进行计算
cars_driven = drivers
carpool_capacity = cars_driven*space_in_a_car
average_passengers_per_car = passengers / cars_driven


print "There are",cars,"cars avaiable."
print "There are only",drivers,"drivers avaiable."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."