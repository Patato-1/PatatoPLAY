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
# score = int(input("请输入你的分数"))
# if score > 600:
#     print("欢迎来到学校")
# elif score <= 600:
#     print("兄弟去复读吧")


#项目：结合用户账号密码判断账密码是否正确，都正确登录成功，否则失败；
# a = int(input("请输入账号"))
# b = int(input("请输入密码"))
# if a == 18888 and b == 111:
#     print("登录成功")
# else:
#     print("登录失败")
# 项目：根据用户输入的年份判断是否为闰年；
# year = int(input("请输入年份；"))
# if (year %100 != 0 and year %4 == 0) or year %400 == 0:
#     print(f"{year},是闰年")
# else:
#     print(f"{year},是平年")
# 练习；
# num = int(input("请输入数字；"))
# if num %2 == 0:
#     print("是偶数")
# else:
#     print("是奇数")

# num = int(input("请输入数字；"))
# if num >= 18:
#     print("成年人")
# else:
#     print("未成年人")
# num = int(input("请输入数字；"))
# if num > 0:
#     print("正数")
# elif num < 0:
#     print("负数")
# num = int(input("请输入数字；"))
# if num >= 60:
#     print("及格")
# else:
#     print("不及格")
#
# a = input("请输入账号；")
# b = int(input("请输入密码；"))
# if a == "admin" and b == 666888:
#     print("登录成功")
# elif a == "root" and b == 123456:
#     print("登陆成功")
# elif a == "zhangsan" and b == 123321:
#     print("登陆成功")
# else:
#     print("登陆失败")
# num = int(input("请输入金额"))
# if num >= 500:
#     print("应付",num * 0.8)
# else:
#     print("实付",num)
# a = int(input("请输入第一条边"))
# b = int(input("请输入第二条边"))
# c = int(input("请输入第三条边"))
# if a + b > c and a + c > b and b + c > a:
#     if a==b and b==c:
#         print(f"{a}{b}{c}三条边组成的三角形是等边三角形")
#     elif a==b or b==c or a==c:
#         print(f"{a}{b}{c}三条边组成的三角形是等腰三角形")
#     else:
#         print(f"{a}{b}{c}三条边组成的三角形是普通三角形")
# else:
#     print(f"{a}{b}{c}不构成三角形")
# c = int(input("请输入用电度数"))
# if c<=2880:
#     print(f"电费应付：{c * 0.4883} ")
# elif  c <=4800:
#     print(f"电费应付：{c * 0.5383} ")
# elif c> 4800:
#     print(f"电费应付：{c* 0.7883} ")
# # 纠正；
# 获取用电度数
# power = int(input("请输入年度用电度数："))
# fee = 0
#
# if power <= 2880:
#     # 第一档
#     fee = power * 0.4883
# elif power <= 4800:
#     # 第二档：2880度低价 + 超出部分中价
#     fee = 2880 * 0.4883 + (power - 2880) * 0.5383
# else:
#     # 第三档：三部分分别计价
#     fee = 2880 * 0.4883 + (4800 - 2880) * 0.5383 + (power - 4800) * 0.7883
#
# print("年度总电费：", fee)
# mach case：项目!!!!!!!!!!!!!!!!!!
# 实现一个计算器，可以实现+-/*运算，用户数日需要运算的两个数以及运算符之后，就可以计算；
# num1 =  float(input("请输入第一个数字: "))
# num2 = float(input("请输入第二个数字: "))
# op = input("请输入+ - * /")
# match op:
#     case "+":
#         print(f"{num1} +{num2} = {num1 + num2 }")
#     case "-":
#         print(f"{num1} -{num2} = {num1 - num2 }")
#     case "*":
#         print(f"{num1} *{num2} = {num1 * num2 }")
#     case "/" if num2 != 0:
#         print(f"{num1} / {num2} = {num1 / num2 }")
#     case _:
#         print("输出错误")

# op = input("请输入玩家指令")
# match op:
#     case "w"|"W"|"上":
#         print("角色向上运动")
#     case "s“|”S"|"下":
#         print("角色向下运动")
#     case "j”|“J”|“攻击":
#         print("角色攻击")
#     case "ESC“|”esc":
#         print("退出")
#     case "a“|”A“|”左":
#         print("角色向左运动")
#     case "d“|”D|“右":
#         print("角色向右运动")
#     case "跳"|" "|"空格":
#         print("角色跳跃")
#     case _:
#         print("无效输出")
# sun = 0
# i = 1
# while i<=100:
#     if i % 2 ==1:
#         sun = sun + i
#     i += 1
# print(f"输出之和是{sun}")

# sum = 0
# i = 1
# while i<= 100:
#     if i % 2 == 0:  # 只有偶数才能通过if，赋值给i的只能是偶数。
#         sum += i    # sum只能是偶数相加，因为奇数通过不了if，所以sum只能两次两次的相加
#     i += 1          # i的累加次数，每次都累加一次
# print(f"所有偶数和是：{sum}")
#
# for循环
# a = input("请输入你要编历的字符串：")
# for s in a:
#     print(f"{s}")
# else:
#     print("输出结束")
# for i in  range(1,10):===================================输出从1到9
#     for j in range(1,i+1):===================================
#         print(f"{i}X{j}={i * j}",end="\t") ===========================end="\t"禁止换行并且空出一格
#
#     print() =================自动换行：

# 案例1打印边长为5的等腰直角三角形
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end = "\t" )
#     print( )
# 案例2做一个数字金字塔；
# for i in range(1,7):
#      for j in range(1,i+1):
#          print(f"{j}",end=" ")
#      print()
# 案例3做一个国际象棋；
# for i in range(8):
#     for j in range(8):
#         if j % 2 == 1:
#             print(1, end=" ")
#         elif j % 2 == 0:
#             print(0, end=" ")
#     print()
#
#需求，用户名密码登录，正确的用户名和密码为admin/666888、zhangge/666888、taoge666/888666有5次登录机会，输入错误5次，不允许在操作了
num = 0
while True:
    if num >= 5:
        print("警告!,不能登录")
        break
    name = input("账号")
    passwork = input("密码")

    if name == "admin" and passwork == "666888":
        print("登录成功")
        break
    elif name == "zhangsan" and passwork == "123456":
        print("登录成功")
        break
    elif name == "taoge" and passwork == "888666":
        print("登录成功")
        break
    elif name == "" or passwork == "":
        print("您的账号密码为空，请重新登录")
        continue
    else:
        print("登录失败请重新登录")
        num = num + 1
        continue
























