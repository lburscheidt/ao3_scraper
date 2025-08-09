import scrapy
from ao3_scraper.items import FicItem
import requests

# from myao3scraper.itemloaders import FicItemLoader
from scrapy.loader import ItemLoader
from time import sleep
from scrapy import Spider, Request
from scrapy.http import FormRequest
from urllib.parse import urlencode
from scrapy.utils.response import open_in_browser
import os


class Ao3spiderSpider(scrapy.Spider):
    name = "loginspider"
    allowed_domains = ["archiveofourown.org"]
    start_urls = ["https://archiveofourown.org/users/login"]

    def parse(self, response):
        csrf_token = response.css("input::attr(value)").get()
        print(csrf_token)
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                "authenticity_token": csrf_token,
                "user[login]": "queerplatonicity",
                "user[password]": "RageDeviationGivingShading",
                "commit": "Log+In",
                "user[remember_me]": "1",
            },
            callback=self.start_scraping,
        )

    def start_scraping(self, response):
        url = "https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=created_at%3A%5B%222025-01-01%22+TO+%222025-01-15%22%5Drestricted%3Afalse&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=created_at&work_search%5Bsort_direction%5D=asc"
        yield scrapy.Request(url=url, callback=self.parse_100)

    def parse_100(self, response):
        print("logged in!")
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
            yield response.follow(next_page_url, callback=self.parse_100)
