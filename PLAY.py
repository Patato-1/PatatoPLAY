# name = "patato"
# #age = 18
# print("大家好我是%s年龄是%s"%(name,age) )
# print(f"大家好我是{name}年龄是{age}")
#
# def cat():
#     print("喵")
# cat()
# def hello(name):
#     print("你好",name)
# hello("patato")
#
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# print(f"你的名字是{name},您的年龄是{age}")
#
# 银行卡ATM取款项目
# TotalBalance=10000
# passwork = input("请输入您的密码：")
# print(f"{passwork}密码正确")
# num = input("请输入您的取款余额")
# print(f"{num}")
# print(f"您取款后的余额为：{TotalBalance - int(num)}")
#
# 项目：根据用户输入的两个数字，计算两个数之和，并将其输出到控制台
# 小明 = input("请输入第一个数字：")
# 小红 = input("请输入第二个数字")
# 总和 = input(int(小明)+int(小红))
# print(f"input（{小明}）+input({小红} ={总和})")
# a = float(input("请输入x的指："))
# b = float(input("请输入y的指："))
# print("x+y=",a%b)
# print("x-y=",a-b)
# 案例1：
# a = int(input("请输入第一个值："))
# b = float(input("请输入第二个值："))
# c = int(input("请输入第三个值："))
# print("abc平均数=",(a+b+c)/3)
#  #案例3：
# import math
# r = float(input("请输入半径："))
# pi = math.pi
# C = 2*pi*r
# S = pi*r**2
# print(f"周长是：{C}" )
# print(f"面积是：{S}")
# num = 20
# num += 10
# print(num)
score = int(input("请输入你的分数"))
if score > 600:
    print("欢迎来到学校")
elif score <= 600:
    print("兄弟去复读吧")