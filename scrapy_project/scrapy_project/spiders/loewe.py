# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.extras import utils
import time
import json


class LoeweSpider(scrapy.Spider):
    name = "loewe"
    allowed_domains = ["www.loewe.com/int/zh_CN"]
    start_urls = ['http://www.loewe.com/int/zh_CN/女士系列/丝巾?iscroll=1']

    def parse(self, response):
        driver = response.driver
        driver.execute_script("var q=document.documentElement.scrollTop=2000000")
        result = {}
        elements = utils.find_elements_by_css_selector(driver,'div.grid-tile.js-slv-elements')
        for element in elements:
            result['link_data'] = LoeweSpider.allowed_domains[0] + json.loads(utils.find_element_by_css_selector(element, 'div.product-tile').get_attribute('data-productjson'))[0].get('productURL')
            yield result
