import sqlite3

books_file = 'books.txt'


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE books(name text, author text, read integer)')

    connection.commit()
    connection.close()

def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    #cursor.execute(f'INSERT INTO books VALUES( "{name}","{author}",0 )')#this is not recommended example: if author= ,0); Drop table books; in this case it will run insert query and also drop query , its not safe to use this way.
    cursor.execute('INSERT INTO books VALUES(?, ?, 0 )',(name, author))
    connection.commit()
    connection.close()

def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]# fetch all gives list of tuple [(name, author, read),(name, author, read)]
    connection.close()
    return books


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = 1
    _save_all_books(books)


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
