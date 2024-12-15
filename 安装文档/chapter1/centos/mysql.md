## Mysql安装

1.查看mysql是否存在，存在先卸载

```
rpm -qa | grep mysql
```

2.下载MySQL仓库并安装

```
wget https://repo.mysql.com//mysql80-community-release-el7-3.noarch.rpm
```

```
yum -y install mysql80-community-release-el7-3.noarch.rpm
```

3.默认安装MySQL8.0，如果需要使用MySQL5.7的话需要修改/etc/yum.repos.d/mysql-community.repo配置文件

将mysql80中enabled属性改为0，并添加图中红框内代码\(安装MySQL8.0跳过该步骤\)

4.安装MySQL数据库

```
yum -y install mysql-community-server
```

5.开启mysql服务

```
systemctl start mysqld.service
```

6.查看mysql默认密码并登陆

```
cat /var/log/mysqld.log | grep password
```

```
mysql -uroot -p
```

7.修改初始密码（若想改为弱密码）

```
SHOW variables LIKE 'validate_password%';
```

注：有可能遇到情况，此时先修改密码为强密码，便可以继续进行修改密码验证策略操作

将密码验证策略改为LOW，密码长度4位以上

```
1 set global validate_password.policy=0;
2 set global validate_password.length=4;    #重启MySQL后失效
```

此时再进行修改密码操作，可以修改为弱密码了

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your password';
set password = 'your password';                                #两种命令二选一进行修改密码
```

以后便可以使用你自己设置的密码登陆

8.设置远程连接\(前提：关闭防火墙或开放3306端口\)

在实际工作中，经常会用到诸如DBeaver等的数据库管理工具进行远程连接mysql数据库，需要设置允许远程连接。

在mysql数据库的user表中查看host，默认只允许localhost访问

只需将localhost改为%允许任意地址访问即可

```
update user set host = '%' where user = 'root';
flush privileges;             # 刷新权限 权限更新后刷新才会起作用
```

注：如果使用客户端连接提示了plugin caching\_sha2\_password错误，这是因为MySQL8.0的密码策略默认为caching\_sha2\_password\(MySQL5.7无此问题\)

```
update user set plugin = 'mysql_native_password' where user = 'root';
flush privileges;             # 刷新权限 权限更新后刷新才会起作用
```

如果使用DBeaver建立MySQL 8+连接，无需修改默认密码策略，但可能会提示Public Key Retrieval is not allowed错误

这是因为MySQL8.0的密码策略默认为caching\_sha2\_password认证，密码在传输过程中必须使用 SSL 协议保护，但是如果 RSA 公钥不可用，可以使用服务器提供的公钥；需要修改AllowPublicKeyRetrieval=True参数以允许客户端从服务器获取公钥，在Dbeaver的修改如下：

修改完成后可以正确建立远程连接

9.my.cnf配置文件

前言：若rpm安装无/etc/my.cnf文件，需将/usr/share/mysql目录下配置文件复制至/etc目录下

```
cp /usr/share/mysql/my-large.cnf /etc/my.cnf
```

\[client\]

port = 3306

socket = /var/run/mysql/mysql.sock

\[mysqldump\]

quick

max\_allowed\_packet = 16M

以上参数会被 MySQL 客户端应用读取，参数说明如下：

* port：MySQL 客户端连接服务器端时使用的端口号，默认为 3306
* socket：套接字文件所在目录
* quick：支持较大的数据库转储，导出非常巨大的表时需要此项。
* max\_allowed\_packet：服务所能处理的请求包的最大大小以及服务所能处理的最大的请求大小（当与大的BLOB字段一起工作时相当必要），每个连接独立的大小，大小动态增加。

\[mysqld\]

user = mysql

basedir = /usr/local/mysql

datadir = /mydata/mysql/data

port = 3306

server-id = 1

socket = /var/run/mysql/mysql.sock

上述参数说明如下：

* user：mysqld 程序在启动后将在给定 UNIX/Linux 账户下执行。mysqld 必须从 root 账户启动才能在启动后切换到另一个账户下执行。mysqld\_safe 脚本将默认使用 user=mysql 选项来启动 mysqld 程序。
* basedir：指定 MySQL 安装的绝对路径；
* datadir：指定 MySQL 数据存放的绝对路径；
* port：服务端口号，默认为 3306
* server-id：MySQL 服务的唯一编号，每个 MySQL 服务的 id 需唯一。
* socket：socket 文件所在目录

character-set-server = utf8mb4

collation-server = utf8mb4\_general\_ci

init\_connect = 'SET NAMES utf8mb4'

lower\_case\_table\_names = 1

key\_buffer\_size = 16M

max\_allowed\_packet = 8M

no-auto-rehash

sql\_mode=TRADITIONAL

skip-grant-tables

* character-set-server：数据库默认字符集
* collation-server：数据库字符集对应一些排序等规则，注意要和character-set-server对应
* init\_connect：设置client连接mysql时的字符集，防止乱码
* lower\_case\_table\_names：是否对sql语句大小写敏感，1表示不敏感\(MySQL8.0+需要初始化之前设置\)
* key\_buffer\_size：用于指定索引缓冲区的大小
* max\_allowed\_packet：设置一次消息传输的最大值
* no-auto-rehash：仅仅允许使用键值的UPDATES和DELETES
* sql\_mode：表示 SQL 模式的参数，通过这个参数可以设置检验 SQL 语句的严格程度
* skip-grant-tables：跳过密码验证 \(平时不要开启，忘记root密码时再使用\)

忘记root密码时：

重置root密码为空\(开启skip-grant-tables\)

```
UPDATE mysql.user SET authentication_string = '' WHERE user = 'root';
```



****