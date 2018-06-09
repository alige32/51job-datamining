# -*- coding:utf-8 -*-
import scrapy
from job.items import JobItem, DescItem
import sys
import logging

reload(sys)
sys.setdefaultencoding('utf-8')


class Job51Spider(scrapy.Spider):
    name = 'job51'
    allowed_domains = ['www.51job.com', 'jobs.51job.com']
    start_urls = [
        'https://search.51job.com/list/040000%252C030200,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E6%258C%2596%25E6%258E%2598,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(
            i) for i in range(1, 14)]

    def parse(self, response):
        node_list = response.xpath("//div[@class='el' and not(@id)]")

        for node in node_list:
            item = JobItem()

            item["position_name"] = node.xpath("./p[@class='t1 ']/span/a/@title").extract_first()
            item["position_link"] = node.xpath("./p[@class='t1 ']/span/a/@href").extract_first()
            item["company_name"] = node.xpath("./span[@class='t2']/a/@title").extract_first()
            item["postiton_pay"] = node.xpath("./span[@class='t4']/text()").extract_first()
            item["work_location"] = node.xpath("./span[@class='t3']/text()").extract_first()
            item["publish_times"] = node.xpath("./span[@class='t5']/text()").extract_first()
            yield item
            # item 数据交给管道处理（需要自己实现）
            # Request数据交给调度器处理（框架已经实现）
            logging.info(item['position_link'])
            logging.info(type(item['position_link']))
            yield scrapy.Request(item['position_link'], callback=self.parse_page)
            # yield item

    def parse_page(self, response):
        item = DescItem()
        # print response
        tl = response.xpath("//div[@class='bmsg job_msg inbox']//text()").extract()
        ts = ''.join(tl)
        logging.info(type(ts))
        ts = ts.replace('\n', '').replace('\t', '').strip().split('分享')
        logging.info(ts[0])
        logging.debug('数据类型是:{}'.format(type(ts[0])))
        item["position_desc"] = ts[0]
        logging.info('item是{}'.format(item['position_desc']))
        item["position_demand"] = ''
        yield item
