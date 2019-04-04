import sqlite3

books_file = 'books.txt'


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text, author text, read integer)')

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


def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,)) # comma beside name is indicate its a tuple
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books  WHERE name=?',(name,)) # comma beside name is indicate its a tuple
    connection.commit()
    connection.close()


# def delete_book(name):
#     for book in books:
#         if book['name'] == name:
#             books.remove(book)
