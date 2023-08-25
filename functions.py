import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error:
        print(Error)
    return conn

def create_connection_in_memory():
    conn = None
    try:
        conn = sqlite3.connect(":memory:")
        return conn
    except Error:
        print(Error)
    return conn


def execute_sql(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error:
        print(Error)
        
def add_book_genre(conn, genre):
    pass
    sql = '''
        INSERT INTO genres (genre, description)
        VALUES (?, ?)
        '''
    cur = conn.cursor()
    cur.execute(sql, genre)
    conn.commit()
                
def add_book_genres(conn, genres_list):
    for genre in genres_list:
        add_book_genre(conn, genre)

def add_book(conn, book):
    sql = '''
        INSERT INTO books (title, author, year, genre)
        VALUES (?, ?, ?, ?)
        '''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()

def add_books(conn, books_list):
    cur = conn.cursor()
    cur.executemany('''
        INSERT INTO books (title, author, year, genre)
        VALUES (?, ?, ?, ?)
                ''', books_list)
    conn.commit()
