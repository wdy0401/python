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

