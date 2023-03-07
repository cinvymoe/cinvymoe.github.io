---
layout:     post
title:      Alist docker
subtitle:   Alist docker
date:       2022-11-04
author:     Cinvy
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - AList
    - Docker
---

## 一、安装Docker+AList
在官网下载Docker Desktop安装包后安装。
在windows搜索栏搜索并运行终端。
在终端中输入以下命令行以安装alist，其中D盘(/D/)可以替换为其他磁盘。（如果失效则访问参考文档Use Docker | AList Docs）  
`docker run -d --restart=always -v /E/alist:/opt/alist/data -p 5244:5244 --name="alist" xhofe/alist:latest`  
继续在终端中输入以下命令行获取到password。（记住此password）
docker exec -it alist ./alist admin


浏览器访问 http://127.0.0.1:5244/ 点击网页下方的管理。
输入admin和刚刚记住的password并登录。
如果能登录成功，说明docker+alist部署成功。

## 网盘添加到AList
https://alist-doc.nn.ci/docs/driver/baidu
https://alist.nn.ci/zh/guide/drivers/aliyundrive.html

## 使用RaiDrive将Quark网盘挂载到本地
安装并打开RaiDrive，点击上方的添加。
服务类型选择NAS->WebDAV，取消勾选地址，账户填（admin,password）然后其他内容照着填。  
**路径选/dav**  
点击连接后不报错，说明已经挂载成功了。
点击右方的齿轮。
点击下方的断开连接。
在高级设置中勾选“复制时尝试保持原修改日期”，然后将容量修改为夸克网盘对应大小（6T填6144，1T填1024，xT填x*1024的值），点击连接。
打开桌面上的“此电脑”，出现以下界面说明所有挂载已经完成了。


