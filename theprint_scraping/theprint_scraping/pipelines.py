# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pyodbc

class TheprintScrapingPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-CJ5FL6B9\SQLEXPRESS;'
                              'Database=theprint_scraping_db;'
                              'Trusted_Connection=yes;')

        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute('''DROP TABLE IF EXISTS defence_articles''')
        self.curr.execute('''
                    create table defence_articles(
                    article_id INT PRIMARY KEY IDENTITY(1,1),
                    article_title VARCHAR(100) NOT NULL,
                    article_author VARCHAR(50) NOT NULL,
                    article_date VARCHAR(20) NOT NULL,
                    );
                    ''')


    def process_item(self, item, spider):
        self.store_data(item)
        print("*****Author is: ", item['author'])
        return item


    def store_data(self, item):
        self.curr.execute("INSERT INTO defence_articles(article_title, article_author, article_date) VALUES (?, ?, ?)", (item['title'], item['author'], item['date']))
        self.conn.commit()