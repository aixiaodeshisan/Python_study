# Python_study
Python,每日打卡学习
# 命名规范
## 1、模块
首字母小写，多单词下划线
>import decoder  
import html_parser  
## 2、类名
驼峰命名法：首字母大写，私有类可用一个下划线开头
>class Farm():  
    pass  
    
>class AnimalFarm(Farm):  
    pass  
    
>class _PrivateFarm(Farm):  
    pass
## 3、函数
函数名一律小写，如有多个单词，用下划线隔开
>def run():  
    pass

>def run_with_env():  
    pass
    
私有函数在函数前加一个下划线_
>class Person():  
    def _private_func():  
       pass     
## 4、变量名
变量名小写, 多单词，用下划线隔开  
```cython
if __name__ == '__main__':
    count = 0
    school_name = ''
```
常量大写，多单词，用下划线隔开
```cython
MAX_CLIENT = 100
MAX_CONNECTION = 1000
```


