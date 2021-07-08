# -*-coding:utf-8-*-
from elasticsearch_dsl import Date, analyzer, Keyword, Text, Document
from elasticsearch_dsl.connections import connections       # 导入连接elasticsearch(搜索引擎)服务器方法

connections.create_connection(hosts=['127.0.0.1'])

ik_analyzer = analyzer('ik_max_word')

class cnblogsType(Document):                     # 自定义一个类来继承DocType类,继承Document的init方法
    # Text类型需要分词,ik_max_wordwei为中文分词器
    title = Text(analyzer="ik_max_word")         # Text为字符串类型并且可以分词建立倒排索引
    description = Text(analyzer="ik_max_word")
    url = Keyword()                              # Keyword为普通字符串类型，不分词
    riqi = Date()
    site = Text()                                # 源网址不用分词

    class Index:
        name = 'cnblogs'
        settings = {
            "number_of_shards": 5,
        }
es = connections.create_connection(cnblogsType)

if __name__ == "__main__":
    cnblogsType.init()                # 生成elasticsearch(搜索引擎)的索引，表，字段等信息