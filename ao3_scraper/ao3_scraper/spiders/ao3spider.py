import scrapy
from ao3_scraper.items import FicItem
import requests

# from myao3scraper.itemloaders import FicItemLoader
from scrapy.loader import ItemLoader
from time import sleep
from scrapy import Spider, Request
from scrapy.http import FormRequest
from urllib.parse import urlencode


# API_KEY = '0228ccf6-1d5c-4b7a-b599-fb5cc79bda5b'
#
# def get_proxy_url(url):
# payload = {'api_key': API_KEY, 'url': url}
# proxy_url = 'https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc' + urlencode(payload)
# return proxy_url
## myspider.py

import random

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363",
]


class Ao3spiderSpider(scrapy.Spider):
    name = "ao3spider"

    start_urls = [
        "https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=created_at%3A%5B%222025-01-21%22+TO+%222025-02-11%22%5D&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=T&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=created_at&work_search%5Bsort_direction%5D=asc"
    ]
    # start_urls = ["https://quotes.toscrape.com/"]

    user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ,Chrome/44.0.2403.157 Safari/537.36"

    # async def start(self):
    #    for url in self.start_urls:
    #        return Request(
    #            url=url,
    #            callback=await self.parse,
    #            headers={
    #                "User-Agent": user_agent_list[
    #                    random.randint(0, len(user_agent_list) - 1)
    #                ]
    #            },
    #        )

    async def parse(self, response):

        fics = response.css("li.work")
        for fic in fics:
            # item = FicItem()
            l = ItemLoader(item=FicItem(), selector=fic)
            # only one value allowed
            l.add_css("work_id_link", 'h4.heading a[href*="/works"]::attr(href)')
            l.add_css("language", "dd.language"),
            l.add_css("word_count", "dd.words"),
            # l.add_css("chapters", "dd.chapters"),
            l.add_css("content_rating", "span.rating span"),
            l.add_css("title", 'h4.heading a[href*="works"]'),
            l.add_css("published_date", "div.header p.datetime"),
            l.add_css("comments", "dd.comments a"),
            l.add_css("hits", "dd.hits"),
            l.add_css("kudos", "dd.kudos a"),

            # more than one value
            l.add_css("authors", 'h4.heading a[href*="users"]'),
            l.add_css("fandoms", "h5.fandoms a"),
            l.add_css("fandom_link", "h5.fandoms a::attr(href)")
            l.add_css("content_warnings", "li.warnings a")
            l.add_css("rpo_categories", "span.category span"),
            l.add_css("characters", "li.characters a"),
            l.add_css("relationships", "li.relationships a"),
            l.add_css("additional_tags", "li.freeforms a"),
            # l.add_css("series", "ul.series a"),
            # l.add_css("series_link", "ul.series a::attr(href)"),
            # l.add_css("part_x_of_series", "ul.series strong"),

            yield l.load_item()
            # self.state["items_count"] = self.state.get("items_count", 0) + 1
        next_page = response.css('[rel="next"] ::attr(href)').get()
        if next_page is not None:
            next_page_url = "https://archiveofourown.org" + next_page
            yield response.follow(next_page_url, callback=self.parse)
