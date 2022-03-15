## 卸载mysql

方法一、

1.查看mysql安装

```
rpm -qa|grep -i mysql
```

2.卸载前关闭mysql服务

```
rpm -ev --nodeps 上面的
```

执行完命令之后再次执行 rpm-qa\|grep -i mysql 会发现已经卸载完成。

执行完命令之后再次执行 rpm-qa\|grep -i mysql 会发现已经卸载完成。

方法二、

执行命令

```
find / -name mysql
```

把查找出的目录删除

rm -rf 上面查出的文件夹

etc/my.cnf 如果存在的话手动删除，这样mysql就卸载完成了。

