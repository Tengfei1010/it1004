#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
 * Created by kevin on 9/23/16.
"""
from datetime import datetime

import scrapy
from bs4 import BeautifulSoup

from .utils import encode_utf8, get_md5_digest
from ..items import ArticleItem
from web.models import Author, Article


class FreeBufSpider(scrapy.Spider):
    name = "安全牛"

    def start_requests(self):
        self.author = Author.query_objects.get(name=self.name)
        self.time_format = '%Y年%m月%d日'
        urls = [
            'http://www.aqniu.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        news = response.css('div.post-text')
        for new in news:
            new_url = new.css('h2 a::attr(href)').extract_first()
            articles = Article.query_objects.filter(
                url_md5=get_md5_digest(new_url))
            if not articles:
                yield scrapy.Request(
                    new_url, callback=self.parse_article_link)

    def parse_article_link(self, response):
        article_item = ArticleItem()
        article = response.xpath('//*[@id="post-content"]')
        article_item['title'] = article.xpath(
            '//*[@id="content"]/div/h1/text()').extract()[0]
        article_time = article.xpath(
            '//*[@id="content"]/div/div[2]/div/span[2]/text()').extract()[0]
        article_item['issue_time'] = datetime.strptime(
            article_time, self.time_format
        )
        article_item['url'] = encode_utf8(response.url)
        article_item['url_md5'] = get_md5_digest(response.url)
        article_item['author'] = self.author

        content = response.xpath('//*[@id="post-content"]').extract()[0]
        soup = BeautifulSoup(content, 'html.parser')
        # delete some div
        soup.find('div', class_='uc-favorite-2 uc-btn').extract()
        soup.find('div', class_='uc-rating').extract()
        article_item['content'] = str(soup)

        yield article_item
