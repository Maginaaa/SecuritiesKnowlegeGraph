# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from securities.spiders.savecsv import save_csv
from securities.items import GetItem


class UserinfoSpider(scrapy.Spider):
    name = 'userinfo'
    allowed_domains = ['pycs.greedyai.com']
    start_urls = ['http://pycs.greedyai.com']

    def parse(self, response):
        body = response.css('body').extract()
        url = re.findall('"\.(.*?html)"', body[0])
        for u in url:
            yield scrapy.Request(url='http://pycs.greedyai.com' + u,callback=self.get_info)


    def get_info(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')

        code = re.findall('\d{6}', soup.head.title.text)[0]
        list = []
        tbody_tag = soup.select('#ml_001 > table > tbody')[0]
        m = 0
        for cd in tbody_tag.children:
            if m % 2 != 0:
                n = 0
                for user_tag in cd.children:
                    if n % 8 == 3:
                        thead_tag = str(user_tag.div.table.thead)
                        name = re.findall('target="_blank">(.*?)</a>', thead_tag)[0]
                        jobs = re.findall('<td class="jobs" style="width: 150px;">(.*?)</td>', thead_tag)[0]
                        intro = re.findall('<td class="intro">(.*?)</td>', thead_tag)[0]
                        sex = re.findall('\u7537|\u5973', intro)[0]
                        age = re.findall('(\d*?)\u5c81', intro)[0]

                        info = GetItem()
                        info['name'] = name
                        info['sex'] = sex
                        info['age'] = age
                        info['code'] = code
                        info['jobs'] = jobs
                        yield info


                        # list.append([name, sex, age, code, jobs])
                        # print(name)
                        # print(sex)
                        # print(age)
                        # print(code)
                        # print(jobs)
                    n += 1
                break
            m = 1

            # if len(list) > 1:
            #     print(list)
            #     save_csv(list)







