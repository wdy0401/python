#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("中文")
print(r'''line 1
line 2
line 3''')
a=1
if a<1:
    print("a<1")
elif a==1:
    print("a==1")
else:
    print("a>1")
    
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

lst=list(range(111))
for x in lst:
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

d={'aa':1,"bb":2}
print(d['aa'])
print('aa' in d)
print("aa",d.get('aa'))
print('cc',d.get('cc',-1))
d.pop('aa')
print('aa',d.get('aa',-1))

lst=[1,2,3,4,5,1]
print(lst)
s1=set(lst)
print(s1)

a=100
print(hex(a))
print(a)

def fun1(x):
	return x*x
print(fun1(2))

def plus(*x):
	ret=0
	for i in x :
		ret=ret+i
	return ret
print(plus(1,2,3,4))

print(lst)
print(lst[0:3])

a="abcdefg"
print(a[3:6])

d={'aa':1,"bb":2}
print(list(d))
for e in sorted(list(d)):
	print(e,d[e])
for e in sorted(list(d.keys())):#与直接使用d相同
	print(e)
for e in sorted(list(d.values())):
	print(e)

def myabs(x):
	return abs(x)
def add(x,y,f):
	return f(x)+f(y)
print(add(1,-1,myabs))
