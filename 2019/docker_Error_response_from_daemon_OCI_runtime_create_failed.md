## docker: Error response from daemon: OCI runtime create failed:

### docker: Error response from daemon: OCI runtime create failed:
```txt
sudo docker run -it --runtime=nvidia --rm darknet:latest bash
docker: Error response from daemon: OCI runtime create failed: container_linux.go:345: starting container process caused "process_linux.go:424: container init caused \"process_linux.go:407: running prestart hook 1 caused \\\"error running hook: exit status 1, stdout: , stderr: exec command: [/usr/bin/nvidia-container-cli --load-kmods configure --ldconfig=@/sbin/ldconfig.real --device=all --compute --utility --require=cuda>=10.1 brand=tesla,driver>=384,driver<385 brand=tesla,driver>=396,driver<397 brand=tesla,driver>=410,driver<411 --pid=15922 /var/lib/docker/overlay2/c64aa99364d4cb0fe7c65856b664064af4f6a240160c6ba2d7ee2d3b8584bda6/merged]\\\\nnvidia-container-cli: initialization error: cuda error: no cuda-capable device is detected\\\\n\\\"\"": unknown.
```

```bash
显示需要驱动程序的所有设备以及适用于它们的软件包
ubuntu-drivers devices

安装显示驱动
sudo apt install nvidia-driver-430

重启系统
sudo reboot
```

### docker: Error response from daemon: OCI runtime create failed
```txt
docker: Error response from daemon: OCI runtime create failed: unable to retrieve OCI runtime error (open /run/docker/containerd/daemon/io.containerd.runtime.v1.linux/moby/7078d5f95f71cbef0f2a1b344248f1337326893353b76939378949ca852a368a/log.json: no such file or directory): exec: "nvidia-container-runtime": executable file not found in $PATH: : unknown.
```

```bash
sudo apt-get install -y nvidia-docker2
```

### 参考资料
* [https://stackoverflow.com/questions/9727688/how-to-get-the-cuda-version](https://stackoverflow.com/questions/9727688/how-to-get-the-cuda-version)
* [Install Nvidia Drivers Ubuntu 18.04](https://www.windowsdigital.com/install-nvidia-drivers-ubuntu-18-04/)
* [NVIDIA NVML Driver/library version mismatch](https://stackoverflow.com/questions/43022843/nvidia-nvml-driver-library-version-mismatch)
* [How To Install Latest NVIDIA Drivers In Linux](http://www.linuxandubuntu.com/home/how-to-install-latest-nvidia-drivers-in-linux)
* [How to Install Latest Nvidia Drivers on Ubuntu](https://www.tecmint.com/install-nvidia-drivers-on-ubuntu/)
* [Can not install nvidia-docker2 under Ubuntu18.04 by default](https://github.com/NVIDIA/nvidia-docker/issues/887)
* [command "docker run --runtime=nvidia --rm nvidia/cuda:9.0-base nvidia-smi" fails with Erro...](https://devtalk.nvidia.com/default/topic/1046289/cuda-setup-and-installation/command-quot-docker-run-runtime-nvidia-rm-nvidia-cuda-9-0-base-nvidia-smi-quot-fails-with-error-/)
