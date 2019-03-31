# Python的数据类型

## 基本数据类型

* 整数（int）    eg: 8
* 浮点数（float）  eg: 8.8
* 字符串（str）  eg: "Python"
* 布尔值（bool）  eg:  True False

**判断数据类型**

``` python
type(8)  # class 'int',type函数判断数据类型
type("python")  # class 'str'
a = 111
isinstance(a, int) //True
```

isinstance 和 type 的区别在于：

- type()不会认为子类是一种父类类型。
- isinstance()会认为子类是一种父类类型。

数据类型转换**

``` python
 int('8')  # 8 , "8"  -> 8
 str(123)  # '123' 
 bool(8)  # True
```



## 变量

``` python
   a        =         123
# ---      ---       -----
#变量名   为变量赋值   变量的值
  b = a # 变量a的值赋给变量b
```

比如：

``` python
print(100/8)
```

​     ↓

``` python
bandwidth = 100
ratio = 8

print(bandwidth/ratio)
```





### 多个变量赋值

Python允许你同时为多个变量赋值。例如：

```python
a = b = c = 1
```

也可以为多个对象指定多个变量。例如：

```python
a, b, c = 1, 2, "runoob"
```

以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

您也可以使用del语句删除一些对象引用。

del语句的语法是：

```python
del var1[,var2[,var3[....,varN]]]
```

您可以通过使用del语句删除单个或多个对象。例如：

```python
del var
del var_a, var_b
```

### 数值运算

## 实例

``` python
5 + 4  # 加法  9
4.3 - 2 # 减法 2.3
3 * 7  # 乘法  21
2 / 4  # 除法，得到一个浮点数  0.5
2 // 4 # 除法，得到一个整数  0
17 % 3 # 取余   2
2 ** 5 # 乘方   32
```

**注意：**

- 1、Python可以同时为多个变量赋值，如a, b = 1, 2。
- 2、一个变量可以通过赋值指向不同类型的对象。
- 3、数值的除法包含两个运算符：**/** 返回一个浮点数，**//** 返回一个整数。
- 4、在混合计算时，Python会把整型转换成为浮点数。