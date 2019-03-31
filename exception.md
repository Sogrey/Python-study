# 异常

异常   !=  错误



异常是在程序出现错误时采取的正常控制流意外的动作。

异常处理的一般流程：

- 检测错误，引发异常。
- 对异常进行捕获的操作。

``` python
try:
    <监控异常>
except Exception[,reason] as e:
    <处理异常>
finally:
    <无论异常是否发生都执行>
```

自定义异常：

``` python
try:
    raise NameError('NameError')
except NameError as e:
    print('is NameError %s' %e)
```

