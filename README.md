## My Blog System - Spider System

> Spider System：Page source from web

- The IP in the IP pool is validated.
- Update once a day
- Is free.


## What does it do?

```
You can get dynamic proxy IP through this interface, and do some crawler operations through these IP addresses.
```

## Dynamic proxy IP pool

**InterFace url**：[this](http://39.106.53.34:10086/getBySize)



### How to use 

参数 | 说明
---|---
size| 获取的IP数目

###### **a example， like this**
- input ：http://39.106.53.34:10086/getBySize?size=3
- then，you can get a string of JSON strings with IP and port ：

```
[
    {
    "ip":"222.85.28.130",
    "port":"40505"
    },
    {
    "ip":"117.91.131.19",
    "port":"9999"
    },
    {
    "ip":"120.83.108.85",
    "port":"9999"
    }
]

```
