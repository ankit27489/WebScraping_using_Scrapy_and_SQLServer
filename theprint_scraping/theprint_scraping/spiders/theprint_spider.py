import scrapy
import pyodbc


# Servername - LAPTOP-CJ5FL6B9\SQLEXPRESS

class ArticleSpider(scrapy.Spider):
    name = 'articles'

    def start_requests(self):
        urls = [
            'https://theprint.in/category/defence/page/1/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for i in range(0, len(
                response.xpath("//div[@class='td_module_11 td_module_wrap td-animation-stack']").extract())):
            headline = response.xpath("//div[@class='td_module_11 td_module_wrap td-animation-stack']/div/h3/a//@title")[i].get()
            author = response.xpath(
                "//div[@class='td_module_11 td_module_wrap td-animation-stack']/div/div/span[@class='td-post-author-name']/a/text()")[
                i].get()
            date = response.xpath("//div[@class ='td_module_11 td_module_wrap td-animation-stack']/div/div/span/time/text()")[i].get()
            yield {'author': author, 'title': headline, 'date': date}
        # page = response.url.split("/")[-2]
        # filename = 'theprint_defence_articles-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)


class DbConn():
    def __init__(self):
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-CJ5FL6B9\SQLEXPRESS;'
                              'Database=theprint_scraping_db;'
                              'Trusted_Connection=yes;')