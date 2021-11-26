#this is the blog Blueprint

from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from users import User
from books import Book
from recommender import *


#without a url_prefix, each of these functions will have their own url
bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()

    #find books for this user
    posts = db.execute(
    " SELECT title, author, rate, b.isbn FROM book b JOIN reviewExp r ON b.isbn = r.isbn WHERE r.user_id = ?", (g.user['tableid'], )).fetchall()

    #if no books to display as read, don't try to recommend
    if not posts:
        bookList = []
    elif (len(posts) < 2):
        bookList = []
    else:
        #get this user, recommend books
        u = User()
        u.getUser(g.user['tableid'], db)
        rec = recommendbook(u, db)

        #construct list of recommended books
        bookList = []
        for i, (rate, isbn) in enumerate(rec):
            book = Book()
            book.isbn_to_book(isbn, db)
            bookinfo = {}
            bookinfo['title'] = book.title
            bookinfo['author'] = book.author
            bookinfo['rate'] = "{:0.1f}".format(rate)
            bookinfo['isbn'] = book.isbn
            bookList.append(bookinfo)

    return render_template('blog/index.html', posts=posts, books=bookList)

@bp.route('/addbook', methods = ('GET', 'POST'))
@login_required
def addbooks():
    if request.method == 'POST':
        title = request.form['title']
        rate = request.form['rate']
        error = None

        db = get_db()
        b = Book()
        b.title_to_book(title, db)
        if b.isbn == None:
            return redirect(url_for('blog.findBook', title=title))

        u = User()
        u.getUser(g.user['tableid'], db)

        if not title:
            title = 'No Title, can\'t save book'

        if not rate:
            error = "No rate, can\'t save book"

        if b.isbn in u.rates:
            error = "Book already in read books!"

        if error is not None:
            flash(error)
        else:

            u.addRates({b.isbn: rate}, db)
            print(u.rates)

            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')

@bp.route('/<title>/addbookrec', methods = ('GET', 'POST'))
@login_required
def addbookrec(title):
    if request.method == 'POST':
        rate = request.form['rate']
        error = None

        db = get_db()
        b = Book()
        b.title_to_book(title, db)

        u = User()
        u.getUser(g.user['tableid'], db)

        if not rate:
            error = "No rate, can\'t save book"
        if b.isbn in u.rates:
            error = "Book already in read books!"

        if error is not None:
            flash(error)
        else:

            u.addRates({b.isbn: rate}, db)
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/addbookrec.html', booktitle=title)

@bp.route('/<title>/findBook', methods = ('GET', 'POST'))
@login_required
def findBook(title):
    if request.method == 'POST':
        author = request.form['author']

        db = get_db()
        b = Book()

        if not author:
            b.findNewBook(title, db)
        else:
            b.findNewBookAuthor(title, author, db)

        return redirect(url_for('blog.addbookrec', title = b.title))
    return render_template('blog/findnewbook.html', booktitle=title)


@bp.route('/<isbn>/deleterec', methods=('GET','POST'))
@login_required
def deleterec(isbn):
    db = get_db()
    b = Book()
    b.isbn_to_book(isbn, db)

    u =  User()
    u.getUser(g.user['tableid'], db)
    u.deleteBook(b.isbn, db)

    db.commit()
    return redirect(url_for('blog.index'))
