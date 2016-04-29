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

    # 关于使用函数逼近行情的看法
    # 1 使用fft
        # 1.1 无法看到趋势项
        # 1.2 低频项
            # 1.2.1   非趋势部分
            # 1.2.2   相位有意义（仅针对第i=1项）
        # 1.3 高频项
            # 1.3.1   噪音
            # 1.3.2   非趋势部分
            # 1.3.3   相位无意义
        # 1.4 对于多阶段，可以通过对比得到市场是否发生了变化
     # 2  使用多项式
        # 2.1 有趋势项
        # 2.2 病态矩阵问题
     # 3  使用正交多项式
        # 3.1 如何处理数据以便使用正交多项式
        # 3.2 可在一定程度上得到频域信息
    
    
    # 关于使用函数对成交量信息进行分析的看法
    
    # 如何定义利用上述指标定义趋势开始与结束
    