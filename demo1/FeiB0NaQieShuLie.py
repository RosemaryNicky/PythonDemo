#!/usr/bin/python3

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数

# a ,b = 0, 1
a = 0
b = 1
while b < 10:
    print(b)
    # a,b = b, a + b
    n = b
    b = a + b
    a = n