from users import User
from books import Book
from recommender import *
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

apikey =pd.read_csv('apikey.txt')
#print values from DATABASE

conn = sqlite3.connect("instance/bookreviews.db")
cursor = conn.cursor()

#cursor.execute("""DROP TABLE IF EXISTS appUser;""")
#cursor.execute(""" SELECT title, author FROM book b JOIN reviewExp r ON b.isbn = r.isbn WHERE r.user_id = 11676""")
#b = cursor.fetchall()
#print(b)

<<<<<<< HEAD
cursor.execute("DELETE FROM book WHERE (title = ?)", ("Harry Potter and the Deathly Hallows",))
conn.commit()
#b = cursor.fetchall()
#print(b)
=======
#conn.commit()
#conn.close()
cursor.execute("SELECT * FROM appUser")
b = cursor.fetchall()
print(b)
>>>>>>> main


#book tests

b = Book()
'''b.isbn_to_book('0155061224')
print(b.id)
print(b.isbn)
print(b.title)
print(b.author)
print(b.year)

b.id_to_book(225817)
print(b.id)
print(b.isbn)
print(b.title)
print(b.author)
print(b.year)

b.title_to_book(' Harry Potter and the Chamber of Secrets', conn)
print(b.id)
print(b.isbn)
print(b.title)
print(b.author)
print(b.year)
'''

#user tests
u = User()
#u.getUser(278861, conn)
#u.deleteUser(conn)
#cursor.execute('DELETE FROM appUser WHERE (username = ?)', ('test',))
<<<<<<< HEAD
#cursor.execute('SELECT * FROM reviewExp WHERE (id = ?)', (278861,))
#b = cursor.fetchall()
#print(b)
=======
cursor.execute('SELECT * FROM reviewExp WHERE (id = ?)', (278861,))
b = cursor.fetchall()
print(b)
>>>>>>> main
#conn.commit()

'''
u = User()
u2 = User()
u3 = User()
u1 = u.makeUser(conn, age= 34, rates = {'0195153448':3})
u1.addBooks(books = ['0002005018','0060973129','0374157065','0393045218','0399135782','0425176428','0671870432','0679425608','074322678X'], conn=conn)
u1.addRates(rates =  {'0002005018':9,'0060973129':2,'0374157065':7,'0393045218':2,'0399135782':1,'0425176428':4,'0671870432':6,'0679425608':2,'074322678X':8}, conn=conn)
print(len(u1.rates))
print(len(u1.books))
u1.deleteBook('0195153448' ,conn)
print(len(u1.rates))
print(len(u1.books))
#u1.recommend()
u1.deleteUser(conn)
'''


#clean up appUser tests
'''
cursor.execute('SELECT * FROM appUser')
b = cursor.fetchall()
print(b)
#cursor.execute('DELETE FROM appUser WHERE (username = ?)', ('test3',))
#conn.commit()
cursor.execute('SELECT * FROM appUser')
b = cursor.fetchall()
print(b)
'''

#recommender tests
'''
user1 = User()
user1.getUser(11676, conn)

rec = recommendbook(user1, conn, 10)

for i, (rate, isbn) in enumerate(rec):
    book = Book()
    book.isbn_to_book(isbn, conn)
    print("{} {} (expected rating {:0.2f})".format(i+1, book.title, rate))
'''
<<<<<<< HEAD

title = 'Columbus Day'
titlestr = title.replace(' ', '+')

url = "https://www.googleapis.com/books/v1/volumes?q=intitle:"+titlestr+"+inauthor:craig+alanson&key="+apikey['key'][0]

loaded = requests.get(url).text

html = json.loads(loaded)
print(html['items'][0]['volumeInfo']['title'])
print(html['items'][0]['volumeInfo']['publishedDate'][:4])
print(html['items'][0]['volumeInfo']['authors'][0])
print(html['items'][0]['volumeInfo']['industryIdentifiers'][1]['identifier'])

#title2 = 'Harry Potter and the Deathly Hallows'
#b = Book()
#b.title_to_book(title2, conn)
#print(b.title)
#print(b.author)
#print(b.isbn)
#print(b.year)
=======
>>>>>>> main
