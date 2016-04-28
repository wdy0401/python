import sys
import math
import numpy
while True:
    line = sys.stdin.readline() # 一次只读一行
    if not line: # 如果是空行(^Z)就停止
        break
#    print(help(line))
    a = line.split() 
#    print(int(a[0]) + int(a[1])) # 否则回显，再回去读下一行
    line_int=[int(x) for x in a]
    cabs=[math.sqrt(x.real**2+x.imag**2) for x in list(numpy.fft.fft(line_int))]
    print(cabs)
    #print(np.fft.fft(line))
	