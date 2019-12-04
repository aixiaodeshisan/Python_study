#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@文件    :basic_question_1.py
@说明    :基础练习100道---01数字组合
@时间    :2019/11/28 21:03:27
@作者    :MrShiSan
@版本    :1.0
'''
import time

def test_method_timer(func,*args):
    "测试某方案运行时间,调用函数的函数,args是元组"
    print("Begin")
    if len(args) == 1:
        start_tim = time.time() 
        func(args[0])
        end_tim = time.time()
        pass
    elif len(args) == 2:
        start_tim = time.time() 
        func(args[0],args[1])
        end_tim = time.time()
        pass
    print("End,运行耗时 = %.8f s" % (end_tim - start_tim))
    pass

def  factorial(n,method = 1): 
    "求阶乘"
    res = 1

    if method == 1:                                              # 方案1，for循环
        for i in range(n-1):                                     # 只乘到2
            res *= n
            n -= 1
            # print("i = %d,res = %d" % (i,res))

    elif method == 2:                                           # 方案2，while循环
        while n>1:
            res *= n
            n -= 1
            # print("n = %d,res = %d" % (n,res))

    elif method == 3:                                            # 方案3，迭代
        # print("n = %d" % (n))
        if n == 2:
            return 2
        else:
            return n * factorial(n-1,3)

    return res
    pass

'''
数字组合
有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
'''
def practice0(method = 1):
    "数字组合"
    # 元组初始化数字（因为元组内元素不可更改），列表存储三位数
    src_num = (1,2,3,4)
    dst_num = []

    if method == 1:
        # 查找所有可能，把符合条件的留下
        for i in src_num:
            for j in src_num:
                for k in src_num:
                    if (i != j) and (i != k) and (j != k):
                        str_com = ("%d,%d,%d" % (i,j,k))
                        dst_num.append(str_com)
        print("共有%d中组合，分别是" %(len(dst_num)),dst_num)
    elif method == 2:
    # 组合数求解组合次数
        pass
    pass

if __name__ == "__main__":
    # test_method_timer(factorial,4,3)
    practice0()
    pass