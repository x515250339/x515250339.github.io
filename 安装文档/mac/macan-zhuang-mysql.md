Mac上如何安装Mysql以及可视化工具navicat

安装Mysql
去官网下载https://www.mysql.com



1. 到达官网划到页面最低端，进入社区![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818153531309.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)
2. 建议选择5.5、5.7的稳定版本

![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818153705427.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

​		![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818153852287.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

​				![在这里插入图片描述](https://img-blog.csdnimg.cn/20200818154009913.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

下载好后
双击

![](https://img-blog.csdnimg.cn/20200818154727718.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)


如果出现了下面的情况无法打开，就打开电脑的系统偏好设置>安全与隐私>通用>点击仍要打开

![](https://img-blog.csdnimg.cn/2020081815492668.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

打开后

![](https://img-blog.csdnimg.cn/20200818155406172.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

一路按继续就行
⚠️注意安装好后会自动生成一个密码，要记住这个，可以保存到备忘录里

![](https://img-blog.csdnimg.cn/20200818160106809.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

启动Mysql
进入系统偏好设置>MySQL

![](https://img-blog.csdnimg.cn/20200818160508948.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

然后点击启动 Start MySQL Server

![](https://img-blog.csdnimg.cn/20200818160701546.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)

变成这个状态

![](https://img-blog.csdnimg.cn/20200818160811964.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2NvZGVibGFuaw==,size_16,color_FFFFFF,t_70#pic_center)


打开终端配置环境变量

输入

```
cd /usr/local/mysql/bin
```

进入mysql文件下的bin目录

bash终端输入

```
open ~/.bash_profile
```

 zsh终端输入

```sh
open ~/.zshrc
```

以此打开.zshrc文件


往.zshrc文件文件中添加以下代码，以此来配置环境变量

```shell
export PATH=$PATH:/usr/local/mysql/bin
alias mysql=/usr/local/mysql/bin/mysql
alias mysqladmin=/usr/local/mysql/bin/mysqladmin
```


添加好后，按`command+S`快捷键保存文件

添加好后，按command+S快捷键保存文件

终端继续输入

```
source ~/.bash_profile
```

 或 

```
source ~/.zshrc
```

然后登录mysql

```sql
mysql -uroot -p
```


输入之前保存的密码

给mysql设置新密码,一般改成123456

```sql
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('你的新密码');
```


设置好后，输入quit退出

安装可视化工具
百度网盘链接: 链接: https://pan.baidu.com/s/17XAT95XL1MWuaTRcnlMmgw 提取码: aw74
里面的dmg、zip文件打开密码均是xclient.info

下载好后安装

点击Connection,选择MySQL


下面的Password就是上面设置的123456

汉化
在上面的网址中下载好对应的汉化包，或用网盘中下载好的汉化包


 解压得到一个文件夹


command+C复制这个文件夹，到应用程序找到安装好的navicat，打开其包目录


进入Contents>Resources,cmmand+V粘贴到Resources目录下



重启navicat，汉化完成
