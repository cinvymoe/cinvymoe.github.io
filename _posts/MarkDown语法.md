---
layout:     post
title:      MarkDown语法
subtitle:   MarkDown语法
date:       2022-11-04
author:     Cinvy
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - MarkDown

---

# 标题

# 一级标题

## 二级标题

### 三级标题

## 链接

[ReactiveCocoa进阶思维导图](https://ww3.sinaimg.cn/large/006y8lVagw1fbgye3re5xj30je0iomz8.jpg)

## 图片

![SNOW_BEAR](https://github.com/cinvymoe/cinvymoe.github.io/blob/master/img/snow_bear.jpg)

### 列表

* 这是无序列表1
- 这是无序列表2
+ 这是无序列表3
1. 这是有序列表1 
2. 这是有序列表2
3. 
* 1. 有序无序混合使用1
+ 2. 有序无序混合使用2

### 表格

| 水果名称 | 价格  | 数量  |
|:----:|:---:|:---:|
| 香蕉   | $1  | 5   |
| 苹果   | $1  | 6   |
| 草莓   | $1  | 7   |

### 引用

> 文字引用 
> 文字引用 
> 文字引用 
> 文字引用 
> 文字引用 
> 
> 文字引用 
> 文字引用 
> 文字引用 

> > > 第一层嵌套引用
> > > 第二层嵌套引用
> > > 第三层嵌套引用

## 代码框

```
    [_textField.rac_textSignal subscribeNext:^(id x) {

    // 在返回结果后，拼接 输出：
    NSLog(@"输出:%@",x);

    }];
```

Use the `printf()
adfjal` function.

***

### 强调

*single asterisks*  
​
_single underscores_  

​
__double underscores__  
**double asterisks**  

单个回车视为空格。

连续回车
才能分段。

行尾加两个空格，这里->  
即可段内换行。