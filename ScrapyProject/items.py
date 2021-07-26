#【定义数据】
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
#定义一个类DoubanItem，它继承自scrapy.Item
    title = scrapy.Field()
    #定义书名的数据属性
    publish = scrapy.Field()
    #定义出版信息的数据属性
    score = scrapy.Field()
    #定义评分的数据属性
