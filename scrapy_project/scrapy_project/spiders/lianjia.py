# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.extras import utils


class LianjiaSpider(scrapy.Spider):
    name = "lianjia"
    allowed_domains = ["sh.lianjia.com"]
    start_urls = []

    def start_requests(self):
        start_urls = ['https://sh.lianjia.com/ershoufang/',
                      'https://sh.lianjia.com/ershoufang/pg2',
                      'https://sh.lianjia.com/ershoufang/pg3',
                      'https://sh.lianjia.com/ershoufang/pg4',
                      'https://sh.lianjia.com/ershoufang/pg5'
                     ]
        for url in start_urls:
            yield scrapy.Request(url.strip(), callback=self.parse)
                 
    def parse(self, response):
        driver = response.driver
        result = {}
        result['url'] = utils.find_element_by_css_selector(driver, 'div.info.clear > div.title > a').get_attribute('href').strip()
        result['title'] = utils.find_element_by_css_selector(driver, 'div.info.clear > div.title > a').text
        result['unitPrice'] = utils.find_element_by_css_selector(driver, 'div.info.clear > div.priceInfo > div.unitPrice').get_attribute('data-price')
        result['area'] = utils.find_element_by_css_selector(driver, 'div.info.clear > div.address > div.houseInfo').text.split('|')[2]
        result['totalPrice'] = utils.find_element_by_css_selector(driver, 'div.info.clear > div.priceInfo > div.totalPrice > span').text
        yield result
