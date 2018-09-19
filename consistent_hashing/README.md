# Consistent Hashing

一致性哈希，最近在招聘Java开发人员，时常会问到他们关于数据库分库分表的一些问题，以及分布式系统（存储）的一些问题。
这些问题的背后都有一个非常重要的算法在使用就是一致性哈希。

通常哈希取模可以完成数据的分散，但是当节点发生变化后原有的哈希记录可能面临全部失效的结果。为了解决这个问题，MIT提出了一致性哈希算法。

### Features
- 支持节点数量变更，避免全部哈希数据失效
- 会有少量数据需要重新迁移
- 节点形成环状，也称为哈希环

![](http://xiaorui.cc/wp-content/uploads/2014/09/20140920083309_49625.gif)

### References

阅读的网络文章如下：

[1](http://www.zsythink.net/archives/1182/)
[2](http://xiaorui.cc/2014/09/20/%E4%BD%BF%E7%94%A8hashring%E5%AE%9E%E7%8E%B0python%E4%B8%8B%E7%9A%84%E4%B8%80%E8%87%B4%E6%80%A7hash/)
[3](https://blog.csdn.net/cywosp/article/details/23397179)

### Package
你可以使用的成熟包：

[hash_ring](https://github.com/Doist/hash_ring)