# Python安装

Python官网：<https://www.python.org/>

PyCharm：<https://www.jetbrains.com/pycharm/>



我这里Python是`v3.7.2`版本，PyCharm选`Community`(免费社区版)。

安装过程很简单，自行实践。

安装成功后，我们可以在命令窗口(Windows 使用 win+R 调出 cmd 运行框)使用以下命令查看我们使用的Python版本：

``` bash
python -V
```

输出：

``` bash
Python 3.7.2
```

## 在 Windows 设置环境变量

在环境变量中添加Python目录：

**在命令提示框中(cmd) :** 输入 

```
path=%path%;C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32
```

> **注意:** `C:\Users\Administrator\AppData\Local\Programs\Python\Python37-32` 是我的Python的安装目录，你可以根据自己的自行配置。

同时建议将Python安装目录下的`Scripts`也添加到环境变量，因为里面有一些有用的Python命令。