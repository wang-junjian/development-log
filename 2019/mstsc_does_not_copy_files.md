# mstsc 不能拷贝文件

* 我远程的时候明明在“本地资源”里面勾选了“剪贴板”，但为什么还不能用，原因就是因为服务器的“rdpclip.exe”这个进程没有正常工作。
```txt
在服务器上杀死进程 rdpclip.exe，然后重新运行 rdpclip.exe
```

## 参考资料
* [远程桌面不能拷贝文件的问题](https://blog.csdn.net/feng_sundy/article/details/50868874)