# Scrapy settings for ao3_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Add Your ScrapeOps API key

SCRAPEOPS_API_KEY = 'YOUR-API-KEY-HERE'


# Add In The ScrapeOps Extension
EXTENSIONS = {
'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}


# Update The Download Middlewares


BOT_NAME = "ao3_scraper"

SPIDER_MODULES = ["ao3_scraper.spiders"]
NEWSPIDER_MODULE = "ao3_scraper.spiders"

ADDONS = {}

LOG_STDOUT=False 
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "ao3_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
USER_AGENT = "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

# Concurrency and throttling settings
# CONCURRENT_REQUESTS = 10
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 5
RANDOMIZE_DOWNLOAD_DELAY = False

AUTOTHROTTLE_ENABLED = False
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_TARGET_CONCURRENCY = 10
AUTOTHROTTLE_MAX_DELAY = 60
# CONCURRENT_ITEMS = 100
REACTOR_THREADPOOL_MAXSIZE = 400
# Hides printing item dict
LOG_LEVEL = "INFO"
RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429]
REDIRECT_MAX_TIMES = 1
# Stops loading page after 5mb
# DOWNLOAD_MAXSIZE = 5592405
# Grabs xpath before site finish loading
DOWNLOAD_FAIL_ON_DATALOSS = False
DEPTH_PRIORITY = 1
# SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue',
# SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# ROTATING_PROXY_LIST_PATH = '/home/max/Desktop/AO3 Data Science From Scratch/proxies.txt' # Path that this library uses to store list of proxies
# NUMBER_OF_PROXIES_TO_FETCH = 20 # Controls how many proxies to use
USER_AGENT = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ,Chrome/44.0.2403.157 Safari/537.36"

# DOWNLOADER_MIDDLEWARES = {
#    'rotating_free_proxies.middlewares.RotatingProxyMiddleware': 610,
#    'rotating_free_proxies.middlewares.BanDetectionMiddleware': 620,
# }

DOWNLOADER_MIDDLEWARES = {
'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}



# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "ao3_stats.middlewares.Ao3StatsSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
# "ao3_stats.middlewares.Ao3StatsDownloaderMiddleware": 543,
# "scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware": 560,
#    "scrapy_cloudflare_middleware.middlewares.CloudFlareMiddleware": 560,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "ao3_scraper.pipelines.Ao3ScraperPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

