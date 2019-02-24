# scrapy-elasticsearch
### Scrapy 爬虫
1.爬取伯乐在线，知乎，拉勾（基于CrawlSpider)，爬取逻辑在spiders包下；items.py里解析，精炼数据，pipelines.py负责数据的写出（数据库（异步），Json格式，elasticsearch）,models包下定义es-Mapping
2.提供了动态变化user-agent,动态ip,爬虫限流，可基于selenium 的 webdriver操作浏览器，针对动态js页面爬取数据
### Elasticsearch
1.LcvSearch包下使用Django框架，从elasticsearch搜索数据，实现一个简单的搜索引擎：包括搜索自动补齐、我的搜索记录、热门搜索、爬取数据总数记录等功能。


## 一个小爬虫demo，学习提升！
