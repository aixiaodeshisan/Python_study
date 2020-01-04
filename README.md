# Python_study

Python,每日打卡学习，先了解Python官方对代码书写上的一些要求

## 命名规范

### 1、模块名（文件被称为模块）、包名

首字母小写，多单词下划线
>import decoder  
import html_parser  

### 2、类名

驼峰命名法：首字母大写，多单词首字母大写(不用下划线分隔)  

#### 普通类

>class Farm():  
    pass  
>class AnimalFarm(Farm):  
    pass  

#### 私有类

>class _PrivateFarm(Farm):  
    pass

### 3、函数

函数名一律小写，如有多个单词，用下划线隔开
>def run():  
    pass
>def run_with_env():  
    pass

私有函数在函数前加一个下划线_
>class Person():  
    def _private_func():  
       pass

### 4、变量名

#### 全局变量名

全大写字母, 多单词，用下划线隔开  

```cython
NUMBER
COLOR_WRITE
```

#### 普通变量名

全小写字母, 多单词，用下划线隔开  

```cython
if __name__ == '__main__':
    count = 0
    school_name = ''
```

#### 实例变量

以 _ 开头，其他和普通变量一样

```cython
_price
_instance_var
```

### 私有实例变量

以 __开头（2个下划线），其他和普通变量一样

``` cython
__private_var
```

### 专有变量

__开头，__结尾，一般为python的自有变量

``` cython
__doc__
__class__
__init__
```
