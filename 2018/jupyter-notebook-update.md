# Jupyter Notebook Update

## 问题
> 编译安装OpenCV3后，导致Python3.6没了，更新成了Python3.7。

```bash
$ jupyter notebook
-bash: /usr/local/bin/jupyter: /usr/local/opt/python3/bin/python3.6: bad interpreter: No such file or directory
```

## 解决
```bash
$ pip3 -U jupyter
```

## 参考资料
* [Jupyter reports “bad interpreter” following Homebrew Python update](https://stackoverflow.com/questions/49097097/jupyter-reports-bad-interpreter-following-homebrew-python-update)
* [IPython 3.5 returns “bad interpreter: No such file or directory”](https://stackoverflow.com/questions/43701835/ipython-3-5-returns-bad-interpreter-no-such-file-or-directory)