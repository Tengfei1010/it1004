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
    name = "FreeBuf"

    def start_requests(self):
        self.author = Author.query_objects.get(name=self.name)
        self.time_format = '%Y-%m-%d'

        urls = [
            'http://www.freebuf.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        news = response.css('div.news-info')
        for new in news:
            new_url = new.css('dl dt a::attr(href)').extract_first()
            articles = Article.query_objects.filter(
                url_md5=get_md5_digest(new_url))
            if not articles:
                yield scrapy.Request(
                    new_url, callback=self.parse_article_link)

    def parse_article_link(self, response):
        article_item = ArticleItem()
        article = response.css('div.articlecontent')
        article_item['title'] = article.css('div.title h2::text').extract_first()
        # time format 2016-09-25
        article_time = article.xpath(
            '/html/body/div[2]/div[1]/div[1]/div[1]/div/div[1]/div/span[3]/text()'
        ).extract()[0]
        article_item['issue_time'] = datetime.strptime(article_time, self.time_format)
        article_item['url'] = encode_utf8(response.url)
        article_item['url_md5'] = get_md5_digest(response.url)
        article_item['author'] = self.author

        content = response.xpath('//div[@id="contenttxt"]').extract()[0]
        soup = BeautifulSoup(content, 'html.parser')
        for img in soup.find_all('img'):
            if img.has_attr('data-original'):
                img['src'] = img['data-original']
        article_item['content'] = str(soup)

        yield article_item
