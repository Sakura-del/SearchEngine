# -*-coding:utf-8-*-
import scrapy

from cnblog.items import CnblogItem,JobboleItem


class Cnblog_Spider(scrapy.Spider):
    name = 'cnblog'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://www.jobbole.com/keji/']

    def parse(self, response):
        divLst = response.xpath('//div[@class = "list-item"]')
        for div in divLst:
            item = JobboleItem()
            item["post_date"] = div.xpath('.//div[@class="about-left"]/span[1]/text()').extract_first()
            num = div.xpath('.//div[@class="about-left"]/span[2]/text()').extract_first().replace('阅读(','').replace(')','')
            item["view_num"]  = int(num)
            item["title"]     = div.xpath('.//div[@class="content-title"]/a/h1/text()').extract_first()
            href = div.xpath('.//div[@class="content-title"]/a/@href').extract_first()
            item["title_link"]= 'http://www.jobbole.com/' + href
            item['category'] = div.xpath('.//div[@class="title-tag "]/text()').extract_first()
            item['category_link'] = response.body_as_unicode()
            item["item_summary"]  = div.xpath('.//div[@class="content-desc shuang"]/text()').extract_first()

            yield item

        # nexturl = response.xpath('.//a[text()="Next >"]/@href').extract_first()
        nexturl = response.xpath('.//a[text()="下一页"]/@href').extract_first()

        if nexturl !='javascript:;':
            # nexturl = 'https://www.cnblogs.com' + nexturl
            nexturl = 'http://www.jobbole.com' + nexturl
            yield scrapy.Request(nexturl,callback=self.parse)

        # divLst = response.xpath('//div[@id="post_list"]/div')
        # for div in divLst:
        #     item = CnblogItem()
        #     item["post_author"] = div.xpath(".//div[@class='post_item_foot']/a/text()").extract_first()
        #     item["author_link"] = div.xpath(".//div[@class='post_item_foot']/a/@href").extract_first()
        #     item["post_date"] = div.xpath(".//div[@class='post_item_foot']/text()").extract()[1].strip().replace('发布于 ',
        #                                                                                                          '')
        #     item["comment_num"] = div.xpath(".//span[@class='article_comment']/a/text()").extract_first()
        #     item["view_num"] = div.xpath(".//span[@class='article_view']/a/text()").extract_first()
        #     item["title"] = div.xpath(".//h3/a/text()").extract_first()
        #     item["title_link"] = div.xpath(".//h3/a/@href").extract_first()
        #     summary_lst = div.xpath(".//p[@class='post_item_summary']/text()").extract()
        #     if len(summary_lst) > 1:
        #         item["item_summary"] = summary_lst[1].strip()
        #     else:
        #         item["item_summary"] = summary_lst[0].strip()
        #     item["digg_num"] = div.xpath(".//span[@class='diggnum']/text()").extract_first()
        #     yield item
        #
        #     nexturl = response.xpath('.//a[text()="Next >"]/@href').extract_first()
        #
        #     if nexturl is not None:
        #         nexturl = 'https://www.cnblogs.com' + nexturl
        #         yield scrapy.Request(nexturl, callback=self.parse)
