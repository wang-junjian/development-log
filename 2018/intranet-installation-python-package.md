# 内网安装Python包

## 下载Python包
* 下载一个包和它的依赖包
```bash
$ pip download package
$ pip download -d . package
```

## 安装本地Python包
* 安装本地包和它的依赖包
```bash
pip install --no-index --find-links . package
```

* 安装本地[wheel](https://pypi.org/project/wheel/)包
```bash
pip install package.whl
```

## 例子
> 基于flask, face-recognition开发的人脸服务(RESTful)。基于macOS在外网下载的，安装到Windows7上

* 下载
```
[Anaconda](https://www.anaconda.com/download/)
[dlib](https://github.com/coneypo/Dlib_install/blob/master/dlib-19.8.1-cp36-cp36m-win_amd64.whl)

pip download flask
pip download flask_apidoc
pip download face_recognition
```

* 安装
```bash
Anaconda

pip install --no-index --find-links . dlib-19.8.1-cp36-cp36m-win_amd64.whl
pip install --no-index --find-links . face_recognition-1.2.3-py2.py3-none-any.whl
pip install --no-index --find-links . flask
pip install --no-index --find-links . flask_apidoc
```

* 设置环境变量PYTHONPATH

## 参考资料
* [pip install](https://pip.pypa.io/en/stable/reference/pip_install/)
* [pip download](https://pip.pypa.io/en/stable/reference/pip_download/)
* [无法连接外网时如何安装Python Package](https://blog.csdn.net/syani/article/details/52775241)
* [python3.6 安装face-recognition竟然如此简单](https://blog.csdn.net/arhatshaw/article/details/80201688)
* [Python 模块](http://www.runoob.com/python/python-modules.html)
* [python 环境变量设置PYTHONPATH](https://www.cnblogs.com/lifeofershisui/p/8135702.html)
