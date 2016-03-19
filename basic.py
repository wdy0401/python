#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#字符串与输出
print("中文")
print(r'''line 1
line 2
line 3''')

#条件判断
a=1
if a<1:
    print("a<1")
elif a==1:
    print("a==1")
else:
    print("a>1")
    
#遍历list与tuple
#list是[] tuple是() tuple可理解为不可变的list
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

#快速列表生成 
#for3.0 range生成的为range，并不是list。
#两者关系类似于 int 与 float。在循环中不区分无妨 在print slice中则要使用list 通过list()转换
sum=0
lst=list(range(1,7,2))#range(1,3)  1 2  range(1,7,2) 1 3 5  
for x in lst:
    sum = sum + x
print(sum)

#循环的使用
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#map的使用
d={'aa':1,"bb":2}
print(d['aa'])
print('aa' in d)
print("aa",d.get('aa'))
print('cc',d.get('cc',-1))
d.pop('aa')
print('aa',d.get('aa',-1))

#list生成与list转set list:数组 set:集合
lst=[1,2,3,4,5,1]
print(lst)
s1=set(lst)
print(s1)

#进制转换
a=100
print(hex(a))
print(a)

#函数定义
def fun1(x):
	return x*x
print(fun1(2))

#数组作为函数参数
def plus(*x):
	ret=0
	for i in x :
		ret=ret+i
	return ret
print(plus(1,2,3,4))

#数组切片与字符串切片
print(lst)
print(lst[0:3])
a="abcdefg"
print(a[3:6])

#使用map中排过序的keys或values
d={'aa':1,"bb":2}
print(list(d))
for e in sorted(list(d)):
	print(e,d[e])
for e in sorted(list(d.keys())):#与直接使用d相同
	print(e)
for e in sorted(list(d.values())):
	print(e)

#函数式编程
def myabs(x):
	return abs(x)
def add(x,y,f):
	return f(x)+f(y)
print(add(1,-1,myabs))

#map reduce
def f(x):
    return x*x
lst=(range(10))
print(lst)
print(list(map(f,lst)))






