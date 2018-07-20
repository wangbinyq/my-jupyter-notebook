# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .models import db, Quote, Tag, QuoteTag, Author


class TutorialPipeline(object):
    def process_item(self, item, spider):
        return item

class Sqlite3Pipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_uri=crawler.settings.get('DB_URI', ':memory:'),
        )

    def __init__(self, db_uri):
        self.db = db
        db.init(db_uri)

    def open_spider(self, spider):
        self.db.connect()
        db.create_tables([Quote, Tag, QuoteTag, Author])

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        name = item.get('author', '')
        text = item.get('text', '')
        tags = item.get('tags', [])
        author, created = Author.get_or_create(name=name)
        quote = Quote.create(text=text, author=author)

        for t in tags:
            tag, created = Tag.get_or_create(name=t)
            QuoteTag.get_or_create(tag=tag, quote=quote)

        return item