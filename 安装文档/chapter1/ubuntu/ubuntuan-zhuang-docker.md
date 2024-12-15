# 1.docker基本原理

https://www.cnblogs.com/xiaonq/p/10241045.html



# 2.ubuntu安装docker

### 2.1 安装docker

```python
# 1.卸载旧版本
sudo apt-get remove docker docker-engine docker.io containerd runc

# 2.更新ubuntu的apt源索引
# 修改apt国内源为中科大源
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/' /etc/apt/sources.list
sudo apt update

#3.安装包允许apt通过HTTPS使用仓库
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

#4.添加Docker官方GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

#5.设置Docker稳定版仓库
#5.1 设置使用官方，很慢
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
#5.2 设置使用阿里云
add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
    
#6.添加仓库后，更新apt源索引
sudo apt-get update

#7.安装最新版Docker CE（社区版）
sudo apt-get install docker-ce

#8.检查Docker CE是否安装正确
sudo docker run hello-world
```

### 2.2 docker默认是国外源可以设置成国内镜像源

```python
root@linux-node1 django-docker]# vim /etc/docker/daemon.json    # 设置docker镜像源
{
    "registry-mirrors": ["http://hub-mirror.c.163.com"]
}

[root@linux-node2 ~]# systemctl daemon-reload                   # 重载文件
[root@linux-node2 ~]# systemctl restart docker                  # 重启docker生效
```

### 2.3 docker启动设置

```python
# 启动Docker服务并设置开机启动
systemctl start docker
systemctl enable docker
```

### 2.4 docker简单使用（创建一个ngixn容器）

```python
# 1、创建一个nginx容器
 docker run -it nginx
 
 # 2、查看docker运行的容器(可以获取到这个容器的id)
 docker ps
 
 # 3、访问这个容器
 # 进入这个nginx容器（进入的文件系统和宿主机是完全隔离的，有自己独立的文件系统）
 docker exec -it 73877e65c07d bash
 
 # 4、查看当前容器的 IP
 docker inspect 73877e65c07d   # 73877e65c07d是通过docekr ps查看到的容器ID
 curl 172.17.0.2               # 测试这个nginx容器是否可以访问
```




