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
    genre TEXT,
    description TEXT)
    """

create_books_table_sql = \
    """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER,
        genre TEXT,
        FOREIGN KEY (genre) REFERENCES genres (id))
    """

execute_sql(conn, create_genres_table_sql)
execute_sql(conn, create_books_table_sql)

# add_book_genre(conn, ('horror', "scary")) # passed argument has to be a tuple



add_book_genres(conn, 
                [('Action and adventure', 'hero, adventure, journey'),
                 ('Comedy', 'funny, parody, excitement'), 
                 ('Crime and mistery', 'crime, criminal, investigation, punishment'), 
                 ('Fantasy', 'magic, creatures, mythology'), 
                 ('Horror', 'fear, dread, terror, monster'), 
                 ('Science fiction', 'futuristic, science, time travel'),
                 ('Romance', 'love, relationship'),
                 ('Scientific', 'science, theory, empiricism'),
                 ('Technical', 'research, experiment, technology')])

the_books_list = [
              ("Don Quixote", "de Cervantes, Miguel", 1605, 'Action and adventure'),
              ("Three Men in a Boat", "Jerome, Jerome K.", 1889, 'Comedy'),
              ("The Hound of the Baskervilles", "Conan Doyle, Arthur", 1902, 'Crime and mistery'),
              ("The Call of Cthulhu", "Lovecraft, H.P.", 1928, 'Fantasy'),
              ("The Witcher", "Sapkowski, Andrzej", 1990, 'Fantasy'),
              ("Misery", "King, Stephen", 1987, 'Horror'),
              ("Frankenstein", "Shelley, Mary", 1816, 'Science fiction'),
              ("Pride and Prejudice", "Austen, Jane", 1813, 'Romance'),
              ("The Selfish Gene", "Dawkins, Richard", 1976, 'Scientific'),
              ("The Singularity is Near", "Kurzweil, Ray", 2006, 'Technical')
                ]

'''
SELECT title, author, year, books.genre, description
FROM books
INNER JOIN genres
ON books.genre = genres.genre
'''


add_books(conn, the_books_list)

sys.exit()

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