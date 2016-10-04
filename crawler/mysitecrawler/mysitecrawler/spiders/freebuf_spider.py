#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 9/23/16.
"""
import scrapy

from

class FreeBufSpider(scrapy.Spider):
    name = "freebuf"

    def start_requests(self):
        urls = [
            'http://www.freebuf.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        news = response.css('div.news-info')[:2]
        for new in news:
            new_url = new.css('dl dt a::attr(href)').extract_first()
            yield scrapy.Request(new_url, callback=self.parse_article)

    def parse_article(self, response):
        article = response.css('div.articlecontent')
        title = article.css('div.title h2::text').extract_first()
        content = response.xpath('//div[@id="contenttxt"]').extract()[0]
        yield {
            'url': response.url,
            'title': title,
            'content': content
        }
