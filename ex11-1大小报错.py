x = raw_input("please input a number")
y = raw_input("please input a number")

 if x >= y:
   print x
 else
   print y
 
 #该段代码是比较两个数的大小并输出较大者，但是当输入x=23，y=100时，输出结果是23；x=3456，y=20000，输出结果数3456。为什么呢？OK，接下来我们利用input()替换raw_input()，继续运行代码，输入x=23，y=100，输出结果是100；x=3456，y=20000，输出结果是20000，结果终于对了，但是为什么利用raw_input()就会出错呢？主要原因是：利用raw_input()进行输入时，可以输入字符以及数字进行比较，比较的根本在于比较二者的ASCII码值，所以当输入x=23,y=100时，计算机就会按顺序一位一位地比较二者的ASCII码值，所以才会输出23。Python2.x版本中raw_input()和Python3.x版本中的input()是一样的，可以接受字符串输入，Python2.x版本中input()只接受阿拉伯数字，输入字符串就会报错。