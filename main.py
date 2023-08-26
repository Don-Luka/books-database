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

genres_list = [('Action and adventure', 'hero, adventure, journey'),
                 ('Comedy', 'funny, parody, excitement'), 
                 ('Crime and mistery', 'crime, criminal, investigation, punishment'), 
                 ('Fantasy', 'magic, creatures, mythology'), 
                 ('Horror', 'fear, dread, terror, monster'), 
                 ('Science fiction', 'futuristic, science, time travel'),
                 ('Romance', 'love, relationship'),
                 ('Scientific', 'science, theory, empiricism'),
                 ('Technical', 'research, experiment, technology')]

books_list = [
              ("Don Quixote", "de Cervantes, Miguel", 1605, 'Action and adventure'),
              ("Three Men in a Boat", "Jerome, Jerome K.", 1889, 'Comedy'),
              ("The Hound of the Baskervilles", "Conan doyle, Arthur", 1902, 'Crime and mistery'),
              ("The Call of Cthulhu", "Lovecraft, H.P.", 1928, 'Fantasy'),
              ("The Witcher", "Sapkowski, Andrzej", 1990, 'Fantasy'),
              ("Misery", "King, Stephen", 1987, 'Horror'),
              ("Frankenstein", "Shelley, Mary", 1816, 'Science fiction'),
              ("Pride and Prejudice", "Austen, Jane", 1813, 'Romance'),
              ("The Selfish Gene", "Dawkins, Richard", 1976, 'Scientific'),
              ("The Singularity is Near", "Kurzweil, Ray", 2006, 'Technical')
                ]

add_book_genres(conn, genres_list)
add_books(conn, books_list)

rows = select_all(conn, 'genres')
for row in rows:
    print(row)

fantasy = select_book_by_genre(conn, 'Fantasy')
for row in fantasy:
    print(row)

selection = select_book_by_key(conn, 'author', 'King, Stephen')
for row in selection:
    print(row)

new_selection = select_where(conn, 'books', author = 'Conan Doyle, Arthur')
for row in new_selection:
    print(row)

update(conn, 'books', 6, author = 'King, James', year = 1957)

new_selection = select_all(conn, 'books')
for row in new_selection:
    print(row)

delete_where(conn, 'books', author = 'King, James')

new_selection = select_all(conn, 'books')
for row in new_selection:
    print(row)
sys.exit()
