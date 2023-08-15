Mac如何安装InfluxDB
打开命令行

```
brew update 

brew install influxdb
```


出现下边这样代表安装成功

![在这里插入图片描述](https://img-blog.csdnimg.cn/2020061010365679.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MTk0ODA3NQ==,size_16,color_FFFFFF,t_70)如果要启动操作系统时，自动启动InfluxDB。则需要运行以下两句命令

出现下边这样代表安装成功
如果要启动操作系统时，自动启动InfluxDB。则需要运行以下两句命令

```sh
ln -sfv /usr/local/opt/influxdb/*.plist ~/Library/LaunchAgents
```



```shell
launchctl load ~/Library/LaunchAgents/homebrew.mxcl.influxdb.plist
```


如果只需要在使用时运行，则运行

```sh
influxd -config /usr/local/etc/influxdb.conf
```



完成后，另开启一个bash工具，执行influx命令，看到如下界面，即为安装成功。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210313194504657.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80NTk1NDEyNA==,size_16,color_FFFFFF,t_70)