# Ubuntu 离线安装 gcc make

## gcc

* 分析依赖包
```bash
apt-get install --simulate gcc

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following additional packages will be installed:
binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-7 gcc-7 gcc-7-base libasan4 libatomic1 libbinutils
libc-dev-bin libc6-dev libcc1-0 libcilkrts5 libgcc-7-dev libgomp1 libisl19 libitm1 liblsan0 libmpc3 libmpfr6 libmpx2
libquadmath0 libtsan0 libubsan0 linux-libc-dev manpages manpages-dev
Suggested packages:
binutils-doc cpp-doc gcc-7-locales gcc-multilib make autoconf automake libtool flex bison gdb gcc-doc gcc-7-multilib
gcc-7-doc libgcc1-dbg libgomp1-dbg libitm1-dbg libatomic1-dbg libasan4-dbg liblsan0-dbg libtsan0-dbg libubsan0-dbg
libcilkrts5-dbg libmpx2-dbg libquadmath0-dbg glibc-doc man-browser
The following NEW packages will be installed:
binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-7 gcc gcc-7 gcc-7-base libasan4 libatomic1 libbinutils
libc-dev-bin libc6-dev libcc1-0 libcilkrts5 libgcc-7-dev libgomp1 libisl19 libitm1 liblsan0 libmpc3 libmpfr6 libmpx2
libquadmath0 libtsan0 libubsan0 linux-libc-dev manpages manpages-dev
0 upgraded, 29 newly installed, 0 to remove and 10 not upgraded.
Inst manpages (4.15-1 Ubuntu:18.04/bionic [all])
Inst binutils-common (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libbinutils (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst binutils-x86-64-linux-gnu (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst binutils (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst gcc-7-base (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libisl19 (0.19-1 Ubuntu:18.04/bionic [amd64])
Inst libmpfr6 (4.0.1-1 Ubuntu:18.04/bionic [amd64])
Inst libmpc3 (1.1.0-1 Ubuntu:18.04/bionic [amd64])
Inst cpp-7 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst cpp (4:7.3.0-3ubuntu2.1 Ubuntu:18.04/bionic-updates [amd64])
Inst libcc1-0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libgomp1 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libitm1 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libatomic1 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libasan4 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst liblsan0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libtsan0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libubsan0 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libcilkrts5 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libmpx2 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libquadmath0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst libgcc-7-dev (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst gcc-7 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Inst gcc (4:7.3.0-3ubuntu2.1 Ubuntu:18.04/bionic-updates [amd64])
Inst libc-dev-bin (2.27-3ubuntu1 Ubuntu:18.04/bionic [amd64])
Inst linux-libc-dev (4.15.0-46.49 Ubuntu:18.04/bionic-updates, Ubuntu:18.04/bionic-security [amd64])
Inst libc6-dev (2.27-3ubuntu1 Ubuntu:18.04/bionic [amd64])
Inst manpages-dev (4.15-1 Ubuntu:18.04/bionic [all])
Conf manpages (4.15-1 Ubuntu:18.04/bionic [all])
Conf binutils-common (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libbinutils (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf binutils-x86-64-linux-gnu (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf binutils (2.30-21ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf gcc-7-base (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libisl19 (0.19-1 Ubuntu:18.04/bionic [amd64])
Conf libmpfr6 (4.0.1-1 Ubuntu:18.04/bionic [amd64])
Conf libmpc3 (1.1.0-1 Ubuntu:18.04/bionic [amd64])
Conf cpp-7 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf cpp (4:7.3.0-3ubuntu2.1 Ubuntu:18.04/bionic-updates [amd64])
Conf libcc1-0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libgomp1 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libitm1 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libatomic1 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libasan4 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf liblsan0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libtsan0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libubsan0 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libcilkrts5 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libmpx2 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libquadmath0 (8.2.0-1ubuntu2~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf libgcc-7-dev (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf gcc-7 (7.3.0-27ubuntu1~18.04 Ubuntu:18.04/bionic-updates [amd64])
Conf gcc (4:7.3.0-3ubuntu2.1 Ubuntu:18.04/bionic-updates [amd64])
Conf libc-dev-bin (2.27-3ubuntu1 Ubuntu:18.04/bionic [amd64])
Conf linux-libc-dev (4.15.0-46.49 Ubuntu:18.04/bionic-updates, Ubuntu:18.04/bionic-security [amd64])
Conf libc6-dev (2.27-3ubuntu1 Ubuntu:18.04/bionic [amd64])
Conf manpages-dev (4.15-1 Ubuntu:18.04/bionic [all])

```

* 下载安装包
```bash
apt-get download binutils binutils-common binutils-x86-64-linux-gnu cpp cpp-7 gcc-7 gcc-7-base libasan4 libatomic1 libbinutils libc-dev-bin libc6-dev libcc1-0 libcilkrts5 libgcc-7-dev libgomp1 libisl19 libitm1 liblsan0 libmpc3 libmpfr6 libmpx2 libquadmath0 libtsan0 libubsan0 linux-libc-dev manpages manpages-dev

apt-get download  gcc
```

* 安装
```bash
dpkg -i *.deb
```

## make

* 分析依赖包
```bash
apt-get install -s make
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Suggested packages:
make-doc
The following NEW packages will be installed:
make
0 upgraded, 1 newly installed, 0 to remove and 10 not upgraded.
Inst make (4.1-9.1ubuntu1 Ubuntu:18.04/bionic [amd64])
Conf make (4.1-9.1ubuntu1 Ubuntu:18.04/bionic [amd64])
```

* 下载安装包
```bash
apt-get download make
```

* 安装
```bash
dpkg -i *.deb
```

## 参考资料
* [Index of /gnu/](https://mirrors.ustc.edu.cn/gnu/)
* [Index of /gnu/gcc](http://ftp.gnu.org/gnu/gcc/)
* [Index of /ubuntu/pool/main/g/gcc-7](http://archive.ubuntu.com/ubuntu/pool/main/g/gcc-7/)
* [软件包: g++ (4:7.3.0-3ubuntu2)](https://packages.ubuntu.com/bionic/g++)
* [软件包: make (4.1-9.1ubuntu1)](https://packages.ubuntu.com/bionic/devel/make)
* [Download Packages With Dependencies Locally In Ubuntu](https://www.ostechnix.com/download-packages-dependencies-locally-ubuntu/)
* [How can I download ubuntu packages in windows to install them on an offline ubuntu machine?](https://superuser.com/questions/393109/how-can-i-download-ubuntu-packages-in-windows-to-install-them-on-an-offline-ubun)
* [InstallingSoftware](https://help.ubuntu.com/community/InstallingSoftware)
* [How can I install software or packages without Internet (offline)?](https://askubuntu.com/questions/974/how-can-i-install-software-or-packages-without-internet-offline)
* [Download and install ubuntu packages and dependencies on a server without internet connection](https://askubuntu.com/questions/811423/download-and-install-ubuntu-packages-and-dependencies-on-a-server-without-intern)
* [源码安装gcc步骤](https://blog.csdn.net/wangqing_12345/article/details/52484723)
* [无外网ubuntu系统下安装gcc make等](https://blog.csdn.net/xuzhouweihao/article/details/26578521)
* [ubuntu18.04安装gcc详细步骤（附问题集）](https://blog.csdn.net/weixin_42108484/article/details/83021957)
* [How to download a software package with all dependencies and sub-dependencies? [duplicate]](https://askubuntu.com/questions/1033682/how-to-download-a-software-package-with-all-dependencies-and-sub-dependencies?noredirect=1&lq=1)
* [Saving deb files from repositories to a custom location for installing offline [duplicate]](https://askubuntu.com/questions/15211/saving-deb-files-from-repositories-to-a-custom-location-for-installing-offline?noredirect=1&lq=1)
