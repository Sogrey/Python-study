# 函数

函数是对程序逻辑结构化的一种编程方法。

## 函数的定义

``` python
def 函数名():
    函数体
    return 需要返回的内容
```

调用时执行：

``` python
函数名()
```



## 函数可变长参数

``` python
def 函数名(frist,* other):
    函数体
    return 需要返回的内容
```

其中 `frist`是必需参数，`other`是可选参数，并且数目可变长。



``` python
def howlong(frist, *other):
    print(1 + len(other))


howlong("hello", 1, '2', 3.2)
// 4
```



## 函数变量作用域

``` python
def func():
    var1 = 456
    print(var1)  # 456


func()
print(var1) # 123
```

函数内的变量作用域只在函数体内有效。

`global`关键字可以让函数内变量变成全局变量，影响函数外变量的值。

``` python
var1 = '123'


def func():
    global var1
    var1 = 456
    print(var1) #456


func()
print(var1) #456
```

# 函数迭代器

``` python
list = [1, 2, 3]
it = iter(list) #迭代器 
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # 3
print(next(it)) # StopIteration,超出范围
```

## 生成器

``` python
for i in range(10, 20, 2):
    print(i)
#10
#12
#14
#16
#18
```

`range`函数第三个参数`step`步长不支持浮点数。



``` python
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x #执行一次到此停止，并记录当前位置，方便下次继续执行
        x += step


for i in frange(10, 12, 0.5):
    print(i)
```

输出：

> 10
> 10.5
> 11.0
> 11.5

## lambda 表达式

``` python
def func(a,b):
    return a+b
```

``` python
lambda a,b:a+b
```

