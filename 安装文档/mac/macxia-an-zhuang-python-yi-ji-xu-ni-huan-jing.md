# 安装

首先我们进入官网下载 对应的版本的 [python](https://www.python.org/downloads/mac-osx/)包 

```
https://www.python.org/downloads/mac-osx/
```

之后进行安装一直下一步傻瓜式安装即可



安装完成之后输入python3 显示对应的版本号则安装成功



之后测试 pip3 输出一堆命令及正确

# 虚拟环境

安装python虚拟环境核心目的就是为了复制一个python环境,这样新项目下载的所有包,都会存放在虚拟环境下的python site-package 中

首先安装

1. sudo pip install virtualenv  # 安装虚拟环境

2. sudo pip install virtualenvwrapper  # 安装虚拟环境扩展包

3. vim .bash_profile  # 家目录下编辑.bash_profile文件,加入以下3句

```js
export WORKON_HOME='~/.virtualenvs'

export VIRTUALENVWRAPPER_PYTHON='/Library/Frameworks/Python.framework/Versions/3.8/bin/python3'

source /Library/Frameworks/Python.framework/Versions/3.8/bin/virtualenvwrapper.sh
```

 `**记得修改版本号为和你相对应得**`



第一句话是 定义虚拟工作目录文件夹的存放位置

 

第二句话是 需要填写 本机python3 的安装位置 具体可以 which python3

![img](https://img2020.cnblogs.com/blog/1141655/202007/1141655-20200703214812596-1986292459.png)

 

第三句话是 需要填写 之前安装的虚拟机的 virtualenvwrapper.sh 的位置 具体可以 which virtualenvwrapper.sh source是更新这个文件使其生效

![img](https://img2020.cnblogs.com/blog/1141655/202007/1141655-20200703214923331-1418455569.png)

 

4. 保存运行这个命令 source ~/.bash_profile

目前为止已经安装完毕,加下来新建工作目录(npy 为新建的虚拟环境)

新建虚拟环境:mkvirtualenv -p python3 npy  #新建成功后,当前路径前面就会有npy

进入虚拟环境工作:workon npy

查看机器上有多少虚拟环境:workon tab按两下

退出虚拟环境:deactivat

删除虚拟环境:rmvirtualenc npy

虚拟环境下安装包:pip install XXX # 前面不能带sudo

查看虚拟环境中安装了哪些python包: pip list



# 更换源

在终端进入目录： `cd ~/.pip/`
如果没有 .pip 文件夹，新建文件夹: `mkdir .pip`
`cd .pip `

```
nano pip.conf
```

粘贴如下内容

> ```
> [global]
> index-url = [http://mirrors.aliyun.com/pypi/simple/](https://link.jianshu.com/?t=http://mirrors.aliyun.com/pypi/simple/)
> [install]
> trusted-host=mirrors.aliyun.com
> ```

或者

清华镜像源

> ```
> [global]
> index-url = [https://pypi.tuna.tsinghua.edu.cn/simple](https://link.jianshu.com/?t=https://pypi.tuna.tsinghua.edu.cn/simple)
> [install]
> trusted-host=pypi.tuna.tsinghua.edu.cn
> ```



mac python 安装-虚拟环境-跟换源 完成