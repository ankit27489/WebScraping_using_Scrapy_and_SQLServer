import pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=LAPTOP-CJ5FL6B9\SQLEXPRESS;'
                              'Database=theprint_scraping_db;'
                              'Trusted_Connection=yes;')

curr = conn.cursor()
curr.execute('''
create table defence_articles(
article_id INT PRIMARY KEY IDENTITY(1,1),
article_title VARCHAR(100) NOT NULL,
article_author VARCHAR(50) NOT NULL,
article_date VARCHAR(20) NOT NULL,
);
''')
conn.commit()
curr.execute("INSERT INTO defence_articles(article_title, article_author, article_date) VALUES (?, ?, ?)", ('SAMPLE_TITLE', 'Ankit Deshmukh', '8 July, 2020'))

conn.commit()
conn.close()