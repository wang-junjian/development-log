# Shell脚本并发执行curl调用人脸识别REST API

## 代码
```shell
#!/bin/bash

num=1

if [ $# -gt 0 ]
then
  num=$1
fi

for i in `seq 1 $num`
do
  curl --data-binary "@/Users/test/111.jpg" -H "Content-Type: application/octet-stream" -X POST http://localhost:5000/face/api/v1.0/identify && echo "Done $i" &
done

wait
```

## 知识点
* 变量定义等于号两边不能有空格 num=1。
* $# 代表传入参数的个数，文件名不算。
* \[] 方括号内要加空格。
* then要另起一行写。
* $0 是文件名。
* $1 是第一个参数。
* curl 最后加一个&，这样代表不等待命令执行完。

## 参考资料
* [Execute curl requests in parallel in bash](https://serverfault.com/questions/456490/execute-curl-requests-in-parallel-in-bash)
* [If Statements!](https://ryanstutorials.net/bash-scripting-tutorial/bash-if-statements.php)
* [Shell script “for” loop syntax](https://stackoverflow.com/questions/1445452/shell-script-for-loop-syntax)
* [Shell Scripting Tutorial](https://www.shellscript.sh/index.html)
* [Writing Your First Script and Getting It to Work](http://linuxcommand.org/lc3_wss0010.php)
* [Shell 传递参数](http://www.runoob.com/linux/linux-shell-passing-arguments.html)