import sys

import sqlite3
from sqlite3 import Error

from functions import *

# conn = create_connection_in_memory()
conn = create_connection("my_books.db")

if conn == None:
    print('Database not found')
    sys.exit()
else:
    pass

# execute_sql(conn, 'USE my_new_database')
execute_sql(conn, 'DROP TABLE IF EXISTS genres')
execute_sql(conn, 'DROP TABLE IF EXISTS books')

create_genres_table_sql = \
    """
    CREATE TABLE IF NOT EXISTS genres (
    id INTEGER PRIMARY KEY,
    genre TEXT)
    """

create_books_table_sql = \
    """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        genre TEXT,
        FOREIGN KEY (genre) REFERENCES genres (id))
    """

execute_sql(conn, create_genres_table_sql)
execute_sql(conn, create_books_table_sql)

# add_book_genre(conn, ('horror',)) # passed argument has to be a tuple

# for gen in ['hor', 'mov']:
#     add_book_genre(conn, (gen,))

add_book_genres(conn, 
                ['Action and adventure',
                 'Comedy', 
                 'Crime and mistery', 
                 'Fantasy', 
                 'Horror', 
                 'Science fiction',
                 'Romance',
                 'Scientific',
                 'Technical'])

add_books(conn,
          [
              ("Misery", "Stephen King", 'Horror'),
              ("The Call of Cthulhu", "H.P. Lovecraft", 'Fantasy')
          ])

sys.exit()

add_book(conn, ("Misery", "Stephen King", 'horror'))
add_book(conn, ("Salsa", 'many', 'salsa'))

cur = conn.cursor()
cur.execute("SELECT * FROM books WHERE genre = 'horror'")
rows = cur.fetchall()
print(rows)

cur = conn.cursor()
cur.execute("SELECT * FROM books WHERE genre = 'salsa'")
rows = cur.fetchone()
print(rows)



# conn = create_connection('my_new_database.db')
# conn.close()