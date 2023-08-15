git 常见错误解决

Failed to connect to github.com port 443: Timed out
git 拉取github代码失败，提示 Failed to connect to github.com port 443: Timed out，取消设置git代理，就可以了。

设置代理
```
git config --global https.proxy [http://127.0.0.1:1080](http://127.0.0.1:1080/)

git config --global https.proxy [https://127.0.0.1:1080](https://127.0.0.1:1080/)
```


取消代理

```
git config --global --unset http.proxy

git config --global --unset https.proxy
```

添加key正确，但是输入命令
```
ssh -T git@github.com
```

得到结果是
Hi xxx! You’ve successfully authenticated, but GitHub does not provide shell access.

解决：输入命令
```
git remote set-url origin git@github.com:名字/仓库名.git
```

OpenSSL SSL_read: Connection was reset, errno 10054 错误解决
```
git config --global http.sslVerify "false"
```