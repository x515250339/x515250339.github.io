# 新机拉取github项目

1. ## git 全局配置 用户名 和 邮箱

   ```bash
   # 用户名
   git config --global user.name 【name】
   # 邮箱
   git config --global user.email 【email】
   # 查看已配置项
   git config --global --list
   # 或者
   git config --list
   ```

   或者查看 本机config文件

   ![image-20211124213033911](新机拉取github项目.assets/image-20211124213033911.png)

2. 接着生成 git 的 ssh 密钥

   ```bash
   ssh-keygen -t rsa -C [email]
   ```

   ![image-20211124213228599](新机拉取github项目.assets/image-20211124213228599.png)

3. 接着在本地查看ssh文件

   ![image-20211124213313817](新机拉取github项目.assets/image-20211124213313817.png)

4. 然后登录 github 操作

   ![image-20211124212848264](新机拉取github项目.assets/image-20211124212848264.png)

   ![image-20211124213455064](新机拉取github项目.assets/image-20211124213455064.png)

5. 将ssh文件中 id_rsa.pub copy 到里面，名称随便起

   ![image-20211124214141600](新机拉取github项目.assets/image-20211124214141600.png)

6. 这就表示成功了

   ![image-20211124214115109](新机拉取github项目.assets/image-20211124214115109.png)

7. 测试 输入，表示成功

   ```bash
   ssh -T git@github.com
   ```

   ![image-20211124214558938](新机拉取github项目.assets/image-20211124214558938.png)

8. 接着clone 项目 就可以了

   ![image-20211124214229587](新机拉取github项目.assets/image-20211124214229587.png)