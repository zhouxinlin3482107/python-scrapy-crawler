# -*- coding: utf-8 -*-
import scrapy
from scrapy_project.extras import utils
import time


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["www.douban.com"]
    start_urls = ['https://www.douban.com/accounts/login']
    

    def parse(self, response):
        driver = response.driver
        result = {}
        search_email = utils.find_element_by_css_selector(driver, 'input#email').send_keys('输入你自己的邮箱')
        utils.sleep(1)
        search_password = utils.find_element_by_css_selector(driver, 'input#password').send_keys('输入你自己的邮箱密码')
        search_captcha = utils.find_element_by_css_selector(driver, '#captcha_image')
        if search_captcha:
            captcha_text = input('Please input the captcha:')
            search_captcha = utils.find_element_by_css_selector(driver, '#captcha_field').send_keys(captcha_text)
            submit = utils.find_element_by_css_selector(driver, 'input.btn-submit').click()
            elements = utils.find_elements_by_css_selector(driver, 'li.rec_topics')
            for element in elements[:-1]:
                result['title'] = utils.find_element_by_css_selector(driver, 'a.rec_topics_name').text 
                result['number'] = utils.find_element_by_css_selector(driver, 'span.rec_topics_subtitle').text
                yield result
        else:
            submit = utils.find_element_by_css_selector(driver, 'input.btn-submit').click()
            elements = utils.find_elements_by_css_selector(driver, 'li.rec_topics')
            for element in elements[:-1]:
                result['title'] = utils.find_element_by_css_selector(element, 'a.rec_topics_name').text
                result['number'] = utils.find_element_by_css_selector(element, 'span.rec_topics_subtitle').text
                yield result
                
                
