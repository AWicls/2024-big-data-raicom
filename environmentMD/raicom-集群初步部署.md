#### raicom-集群初步部署

----

##### **前置环境** 

- Linux-CentOS7操作系统 -- raicom1（10.1.27.142）
- Linux-CentOS7操作系统 -- raicom2（10.1.27.144）
- Linux-CentOS7操作系统 -- raicom3（10.1.27.146）
- SSH远程连接工具 -- FinalShell

##### 1.1 配置主机名（统一）

设置3台机器主机名为：**raicom1、raicom2、raicom3**

```sh
>hostnamectl set-hostname <主机名>
>bash
```

##### 1.2 配置主机映射（统一）

配置主机名与ip映射，把三台都写上，为之后配置ssh主机间免密做准备

```sh
>vi /etc/hosts
```

添加以下内容后保存退出

```properties
10.1.27.142     raicom1
10.1.27.144     raicom2
10.1.27.146     raicom3
```

##### 1.3 关闭防火墙（统一）

关闭防火墙是主机间通信的重要步骤

```sh
>systemctl stop firewalld
>systemctl disable firewalld
```

##### 1.4 配置主机间免密（统一）

###### 1.4.1 生成密钥对

```sh
>ssh-keygen -t rsa
```

###### 1.4.2 复制公钥到其他主机

```sh
>ssh-copy-id raicom1
>ssh-copy-id raicom2
>ssh-copy-id raicom3
```

​    三台统一执行完毕后使用`ssh <主机名>`测试能成功免密登录代表配置成功

---

**前置环境配置完成！**