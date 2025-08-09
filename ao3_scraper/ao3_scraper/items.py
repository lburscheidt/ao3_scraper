# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose, Identity
from w3lib.html import remove_tags
from datetime import datetime
import locale


def convert_to_float(item):
    if len(item) is not 0:
        item = item.replace(",", "")
        # remove_tags(item)
        float(item)
        return item
    else:
        return item


def normalise(item):
    item = item.replace("/", "").lower().strip()
    item = item.replace("&amp;", "&")
    return item


def normalise_relationships(item):
    # item = item.replace("/", "").lower().strip()
    item = item.replace("&amp;", "&").strip()
    return item


def convert_to_date(item):
    date_str = item.replace(" ", "-")
    date_object = datetime.strptime(date_str, "%d-%b-%Y").date()
    return date_object.strftime("%d-%b-%Y")


class Myao3ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class FicItem(scrapy.Item):
    work_id_link = scrapy.Field(
        default=0,
        input_processor=MapCompose(
            remove_tags, lambda x: "https://archiveofourown.org" + x
        ),
        output_processor=TakeFirst(),
    )
    language = scrapy.Field(
        default=0, input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )

    word_count = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, convert_to_float),
        output_processor=TakeFirst(),
    )

    chapters = scrapy.Field(
        default=0, input_processor=MapCompose(remove_tags), output_processor=TakeFirst()
    )
    title = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, normalise),
        output_processor=TakeFirst(),
    )
    authors = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, normalise),
        output_processor=Identity(),
    )
    fandoms = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, normalise),
        output_processor=Identity(),
    )

    fandom_link = scrapy.Field(
        default=0,
        input_processor=MapCompose(
            remove_tags, lambda x: "https://archiveofourown.org" + x
        ),
        output_processor=Identity(),
    )
    content_warnings = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, normalise),
        output_processor=Identity(),
    )
    content_rating = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, normalise),
        output_processor=Identity(),
    )
    rpo_categories = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, normalise),
        output_processor=Identity(),
    )
    characters = scrapy.Field(
        default=0, input_processor=MapCompose(remove_tags), output_processor=Identity()
    )
    relationships = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, normalise_relationships),
        output_processor=Identity(),
    )
    additional_tags = scrapy.Field(
        default=0, input_processor=MapCompose(remove_tags), output_processor=Identity()
    )
    published_date = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, convert_to_date),
        output_processor=TakeFirst(),
    )
    series = scrapy.Field(
        default=0, input_processor=MapCompose(remove_tags), output_processor=Identity()
    )
    series_link = scrapy.Field(
        default=0,
        input_processor=MapCompose(
            remove_tags, lambda x: "https://archiveofourown.org" + x
        ),
        output_processor=Identity(),
    )

    part_x_of_series = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, convert_to_float),
        output_processor=TakeFirst(),
    )

    comments = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, convert_to_float),
        output_processor=TakeFirst(),
    )
    bookmarks = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, convert_to_float),
        output_processor=TakeFirst(),
    )
    hits = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, convert_to_float),
        output_processor=TakeFirst(),
    )
    kudos = scrapy.Field(
        default=0,
        input_processor=MapCompose(remove_tags, convert_to_float),
        output_processor=TakeFirst(),
    )


# class FandomItem(scrapy.Item):
#    name = scrapy.Field()
#    link = scrapy.Field()
