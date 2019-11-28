#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
def practice0():
    s1 = 72
    s2 = 85
    r = (s2 - s1) / s1
    print("小明成绩提升百分点r = %.2f" % r)
    pass

def encode_use():
    print("ord('A')获取字符串整数表示 = ",ord('A'))
    print("chr(66)获取编码对应字符 = ",chr(66))

    print(" 'ABC'.encode('ascii') = ", 'ABC'.encode('ascii'))
    print("'中文'.encode('utf-8') = ",'中文'.encode('utf-8'))

    print("b'ABC'.decode('ascii') = ",b'ABC'.decode('ascii'))
    print(" b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') = ", b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
    print(" b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore') = ", b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
   
    print("len('你好') = ",len('你好'))
    print("len(b'\xe4\xb8\xad\xe6\x96\x87') = ",len('你好'.encode('utf-8')))
    pass

if __name__ == "__main__":
    
    # encode_use()
    practice0()
    pass