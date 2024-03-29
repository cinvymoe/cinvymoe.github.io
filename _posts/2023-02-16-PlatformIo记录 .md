---
layout:     post
title:      PlatformIo记录
subtitle:   PlatformIo记录
date:       2023-02-16
author:     Cinvy
header-img: 
tags:
    - PlatformIo记录
---

## Clangd 
### setting.json配置
```
{
    "clangd.arguments": [
        "--query-driver=/root/.platformio/packages/toolchain-xtensa-esp32/bin/xtensa-esp32*",
        "--header-insertion=never",
        "--all-scopes-completion", // 全局补全(补全建议会给出在当前作用域不可见的索引,插入后自动补充作用域标识符),例如在main()中直接写cout,即使没有`#include <iostream>`,也会给出`std::cout`的建议,配合"--header-insertion=iwyu",还可自动插入缺失的头文件
        "--background-index", // 后台分析并保存索引文件
        "--clang-tidy", // 启用 Clang-Tidy 以提供「静态检查」，下面设置 clang tidy 规则
        "--clang-tidy-checks=performance-*, bugprone-*, misc-*, google-*, modernize-*, readability-*, portability-*",
        "--compile-commands-dir=${workspaceFolder}/", // 编译数据库(例如 compile_commands.json 文件)的目录位置
        "--completion-parse=auto", // 当 clangd 准备就绪时，用它来分析建议
        "--completion-style=detailed", // 建议风格：打包(重载函数只会给出一个建议);还可以设置为 detailed
        // "--query-driver=/usr/bin/clang++", // MacOS 上需要设定 clang 编译器的路径，homebrew 安装的clang 是 /usr/local/opt/llvm/bin/clang++
        // 启用配置文件(YAML格式)项目配置文件是在项目文件夹里的“.clangd”,用户配置文件是“clangd/config.yaml”,该文件来自:Windows: %USERPROFILE%\AppData\Local || MacOS: ~/Library/Preferences/ || Others: $XDG_CONFIG_HOME, usually ~/.config
        "--enable-config",
        "--fallback-style=Webkit", // 默认格式化风格: 在没找到 .clang-format 文件时采用,可用的有 LLVM, Google, Chromium, Mozilla, Webkit, Microsoft, GNU
        "--function-arg-placeholders=true", // 补全函数时，将会给参数提供占位符，键入后按 Tab 可以切换到下一占位符，乃至函数末
        "--header-insertion-decorators", // 输入建议中，已包含头文件的项与还未包含头文件的项会以圆点加以区分
        "--header-insertion=iwyu", // 插入建议时自动引入头文件 iwyu
        "--include-cleaner-stdlib", // 为标准库头文件启用清理功能(不成熟!!!)
        "--log=verbose", // 让 Clangd 生成更详细的日志
        "--pch-storage=memory", // pch 优化的位置(Memory 或 Disk,前者会增加内存开销，但会提升性能)
        "--pretty", // 输出的 JSON 文件更美观
        "--ranking-model=decision_forest", // 建议的排序方案：hueristics (启发式), decision_forest (决策树)
        "-j=12" // 同时开启的任务数量
    ]
}
```
### SSH免密登录
#### 生成密匙对
默认电脑上已经安装了git，没有就先去安装（现在基本都用git了吧）
打开CMD或者git-bash输入以下命令(邮箱改成自己的)

ssh-keygen -t rsa -C “10000@qq.com”

然后敲回车直到完成
秘钥文件默认存在 C:\Users\Administrator\.ssh （Administrator对应你的用户名）

将公钥上传到服务器
将id_rsa.pub重命名为authorized_keys
然后上传到/root/.ssh目录下(没有则新建.ssh目录)
修改vscode ssh_config文件

以下是ssh_config文件配置例子

Host dev
HostName xx.cmtspace.cn
User root
Port 22
PreferredAuthentications publickey
IdentityFile "C:\Users\cinvy\.ssh\id_rsa"

### PlatformIO使用中遇到的坑
https://nu-ll.gitee.io/2021/02/24/PlatformIO%E4%BD%BF%E7%94%A8%E4%B8%AD%E9%81%87%E5%88%B0%E7%9A%84%E5%9D%91/