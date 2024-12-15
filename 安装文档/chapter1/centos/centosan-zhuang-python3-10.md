# centos7 安装python3.10.1

Python官网版本https://www.python.org/downloads/source/

下载.tar.xz包就可以了。其实下面的2个包其一都可以使用
Python-3.10.0.tgz （这个不是编译过的东西，不能解压之后直接使用）
Python-3.10.0.tar.xz (这个是pthon的源码)

## 下载

1. 下载安装包

   ```bash
   wget https://www.python.org/ftp/python/3.10.1/Python-3.10.1.tar.xz
   ```

2. 执行解压命令

   ```bash
   tar -xvJf [文件名]
   ```

## 安装编译相关工具

`在解压后目录中执行`

1. ```bash
   yum -y groupinstall "Development tools"
   ```

2. ```bash
   yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel
   ```

3. ```bash
   yum install libffi-devel -y
   ```

## 编译安装

​	创建编译安装目录

1. ```bash
   mkdir /usr/local/python3
   ```

2. ```bash
   ./configure --prefix=/usr/local/python3
   ```

3. ```bash
   make && make install
   ```


## 创建软连接

1. ```bash
   ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3
   ```

2. ```bash
   ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3
   ```

## 验证

```bash
python3 -V
```

```BASH
pip3 -V
```

<img src="../images/centosan-zhuang-python3-10.assets/image-20211229224858251.png" alt="image-20211229224858251" />

## 修改下载源

1. ```
   cd ~
   ```

2. ```
   mkdir .pip
   ```

3. ```
   cd .pip
   ```

4. ```
   vim pip.conf
   ```

5. ```
   [global]
   
   index-url=http://mirrors.aliyun.com/pypi/simple/
   
   [install]
   
   trusted-host=mirrors.aliyun.com
   ```

   <img src="../images/centosan-zhuang-python3-10.assets/image-20211229224858251.png" alt="image-20211229224858251" style="zoom:100%;" />