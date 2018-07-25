#!/usr/bin/env python
#  -*-coding:utf-8 -*-

# a = 1
# sum = 0
# while(a < 100):
#     sum = sum + a
#     a = a + 1
# print(sum)

# i = 1
# # sum = 0
# # while (i < 100):
# #     if(i%2 == 1):
# #         sum += i
# #     else:
# #         sum -= i
# #     i += 1
# # print(sum)

# username = 'python'
# userpassword = 'python11'
# i = 1
# while i <= 3:
#     name = input('请输入用户名：')
#     password = input('请输入密码：')
#     if name == 'python' and password.upper() == userpassword.upper():
#         print("%s登陆成功" % name)
#         break
#     else:
#         print("用户名或密码错误，请重新输入，您还有%s次机会！" % (3 - i))
#     i += 1
# else:
#     print("三次已过，账户锁定")

# i = 1
# while i < 4:
#     name = input('please enter your username:')
#     psd = input('please enter your password:')
#     if name == 'zhujun'and psd == '123456':
#         print('succeed')
#         break
#     else:
#         print('wrong 您还有%d次机会'%(3-i))
#     i += 1


# username = 'python'
# userpassword = 'python11'
# i = 1
# while i <= 3:
#     name = input('请输入用户名：')
#     password = input('请输入密码：')
#     if name == username and password.upper() == userpassword.upper():
#         print("%s登陆成功" % name)
#         break
#     elif name != username:
#         print("用户名错误，请重新输入，您还有%s次机会！" % (3 - i))
#     else:
#         print("密码错误，请重新输入，您还有%s次机会！" % (3 - i))
#     i += 1
# else:
#     print("三次已过，账户锁定")


# def Login():
#     username = 'python'
#     userpassword = 'python11'
#     i = 3
#     while i > 0:
#         name = input('请输入用户名：')
#         password = input('请输入密码：')
#         if name == username and password.upper() == userpassword.upper():
#             print("%s登陆成功" % name)
#             break
#         elif name != username:
#             print("用户名错误，请重新输入，您还有%s次机会！" % (i - 1))
#         else:
#             print("密码错误，请重新输入，您还有%s次机会！" % (i - 1))
#         i -= 1
#     else:
#         print("三次已过，账户锁定")
#
# Login()




# username = 'python'
# userpassword = 'python11'
# i = 3
# while i > 0:
#     name = input('请输入用户名：')
#     password = input('请输入密码：')
#     if name == username and password.upper() == userpassword.upper():
#         print("%s登陆成功" % name)
#         break
#     elif name != username:
#         print("用户名错误，请重新输入，您还有%s次机会！" % (i - 1))
#     else:
#         print("密码错误，请重新输入，您还有%s次机会！" % (i - 1))
#     i -= 1
# else:
#     print("三次已过，账户锁定")


# def Login():
#     username = 'python'
#     userpassword = 'python11'
#     i = 3
#     while i > 0:
#         name = input('请输入用户名：')
#         password = input('请输入密码：')
#         if name == username and password.upper() == userpassword.upper():
#             print("%s登陆成功" % name)
#             break
#         elif name != username:
#             print("用户名错误，请重新输入，您还有%s次机会！" % (i - 1))
#         else:
#             print("密码错误，请重新输入，您还有%s次机会！" % (i - 1))
#         i -= 1
#     else:
#         print("三次已过，账户锁定")
#
# Login()
