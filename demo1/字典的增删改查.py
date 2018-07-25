#!/usr/bin/env python
# -*- coding:utf-8 -*-

dic = {
    'name' : '老男孩',
    'age':'10000',
    'sex':'男',
}

#增
# dic['hobby'] = 'old_girl'#无责增加，有责修改
# dic['name'] = 'alex'
# print(dic)

#2：
# dic.setdefault('high', 169)#有key则不修改，无责添加。
# print(dic)
# dic.setdefault('name', 'wusir')
# print(dic)
#删
# dic.pop('name')#返回值
# dic.pop('name1',None)
# print(dic)
# print(dic.pop('name'))
# print(dic)

#随机删除popitem
# dic.popitem()
# print(dic)
# print(dic.popitem())

#clear
# dic.clear()
# print(dic)

#del
'''
1,删除整个字典
2，按照键去删除键值对
'''
# del dic
# print(dic)

# del dic['name']
# print(dic)
#改
# dic['name'] = 'alex'#无责增加，有责修改
# dic['hobby'] = 'old_girl'
# print(dic)

# dic = {"name":"jin","age":18,"sex":"male"}
# dic2 = {"name":"alex","weight":75}
# dic2.update(dic)  # 将dic所有的键值对覆盖添加（相同的覆盖，没有的添加）到dic2中
# print(dic)
# print(dic2)

#查
# print(dic['name'])
# print(dic['name1'])
# print(dic.get('name'))
# print(dic.get('name1'), '没有此键...')

# dic.keys()
#
# dic.values()
#
# dic.items()

# print(dic.keys())#类似于列表的一个容器，可以做循环，没有索引
# for i in dic.keys():
#     print(i)
# for i in dic:
#     print(i)

# print(dic.values())

# print(dic.items())

# for i in dic.items():
#     print(i)

# for k, v in dic.items():
#     print(k, v)

dict

#分别赋值
# a, b = 1, 3
# a, b = [22, 33]
# print(a, b)