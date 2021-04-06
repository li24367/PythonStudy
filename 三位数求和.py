m = eval(input("请输入一个三位数:"))
a = int(m/100)
b = int((m-a*100)/10)
c = m % 10
print("和为：",a+b+c)
