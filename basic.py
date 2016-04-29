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

#列表生成器 yield项为生成项 可以不设置终止时刻 也就是生个一个无限长的序列
# y=iter()为generator y=iter为函数
def iter():
    n=1
    while True:
        yield n
        n=n+1
        
y=iter()
while True:
    n=next(y)
    if n>10:
        break
    print(n)
    
#map reduce
def f(x):
    return x*x
lst=(range(10))
print(lst)
print(list(map(f,lst)))
from functools import reduce
def f2(x,y):
    return x+y
print(reduce(f2,map(f,lst)))

#filter
#simple filter
def f3(x):
    return x%2
print(list(filter(f3,range(1,9))))
#prime number
def f1():
	n=2
	while True:
		yield n
		n=n+1
def del_m(n):
	return lambda x:x%n>0
def f2():
	n=f1()
	while True:
		m=next(n)
		yield m
		n=filter(del_m(m),n)
for n in f2():
	print(n)
	if n>10:
		break

#sorted
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L=dict(L)
def by_score(t):
	return L[t]
for i in (sorted(L,key=by_score,reverse=True)):
	print(i,L[i])
for i in (sorted(L,key=lambda x:L[x],reverse=True)):
	print(i,L[i])
	
#closure
def lazy_sum(*args):
	sums=0 # put sums here:  lazysum give the total sum of all given args
	def sum():
		# put sums here: just lazy sum
		nonlocal sums
		for i in args:
			sums+=i
		return sums
	return sum
f=lazy_sum(1,2,3,4,5)
print(f)
print(f())
print(f())

def f5():
	print("func name f5")
	print(f5.__name__)
f5()

#decorator
def pt_1(f):
	def sub_1():
		print("aa")
		f()
	return sub_1
	
@pt_1
def f6():
	print("f6 name "+f6.__name__)
f6()

import functools
def pt_2(ctt):
	def pt_3(f):
		@functools.wraps(f)
		def pt_4():
			print(ctt)
			print("bb")
			f()
		return pt_4
	return pt_3
	
	
@pt_2("b2b")
def f7():
	print("f7 name "+f7.__name__)
f7()

#partial
def f8(a,b):
	return a
f9=functools.partial(f8,2)
print(f9(3))
print(f8(1,2))

#import
import sys
sys.path.append('c:\code\python')
print(sys.path)

import test_w
test_w.print_test()
print('1')

#class
class c1(object):
	__p1=1
	p2=2
	def c1f(self):
		print("c1f")

oc1=c1()
oc1.c1f()
print(oc1.p2)
#print(oc1.__p1) 私有变量 无法访问 

class c2(c1):
	def c1f(self):
		print("c1f c2f")
oc2=c2()
oc2.c1f()
print (isinstance(oc2,c1))
print(type(123))
print(type('123'))
print(type([1,2,3]))
print(type({1,2,3}))
#不宜使用type判断类，or方法等举例如下
print(type(c1))
print(type(oc1))
print(type(c2))
print(type(oc2))
print(type(oc2.c1f))

print(isinstance(oc1,c1))
print(isinstance(oc2,c1))
print(isinstance("ccc",(str,c1)))
print(dir(c1))
print(hasattr(c1,'c1f'))

#实例属性覆盖类属性 删除实例属性后恢复类属性
print(oc1.p2)
oc1.p2=22
print(oc1.p2)
del oc1.p2
print(oc1.p2)

#限制属性范围
class c3(object):
	__slots__=('age',"name")
oc3=c3()
oc3.name="oc3"
#oc3.name1="oc3" 不可 因slots限制了属性的范围  这个限制不会继承给子类

#property
class c4(object):
	__age=0
	@property
	def age(self):
		return self.__age#self 不可缺少
	@age.setter
	def age(self,age):
		self.__age=age

oc4=c4()
print(oc4.age)
oc4.age=10
print(oc4.age)

from enum import Enum,unique
@unique
class wd(Enum):
	W=1
	T=2
d1=wd.W
print(d1)
print(wd.W)
print(d1==1)
print(wd(1))
print(wd(1).value)

#error 
try:
    print(1/0)
except ZeroDivisionError as e:
    print("error",e)
    
    