import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None

    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version: {sqlite3.version}")
        return conn
    except Error:
        print(Error)
    
    return conn

def create_connection_in_memory():
    conn = None

    try:
        conn = sqlite3.connect(":memory:")
        print(f"Connected, sqlite version: {sqlite3.version}")
        return conn
    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
    
    return conn


def execute_sql(conn, sql):
    try:
        with conn:
            conn.execute(sql)
        # c = conn.cursor()
        # c.execute(sql)
    except Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        
def add_book_genre(conn, genre):
    pass
    sql = '''
        INSERT INTO genres (genre, description)
        VALUES (?, ?)
        '''
    with conn:
        conn.execute(sql, genre)
    # cur = conn.cursor()
    # cur.execute(sql, genre)
    # conn.commit()
                
def add_book_genres(conn, genres_list):
    for genre in genres_list:
        add_book_genre(conn, genre)

def add_book(conn, book):
    sql = '''
        INSERT INTO books (title, author, year, genre)
        VALUES (?, ?, ?, ?)
        '''
    with conn:
        conn.execute(sql, book)
    # cur = conn.cursor()
    # cur.execute(sql, book)
    # conn.commit()

def add_books(conn, books_list):
    with conn:
        # conn.execute(sql, book)
        conn.executemany('''
            INSERT INTO books (title, author, year, genre)
            VALUES (?, ?, ?, ?)
                    ''', books_list)
    # cur = conn.cursor()
    # cur.executemany('''
    #     INSERT INTO books (title, author, year, genre)
    #     VALUES (?, ?, ?, ?)
    #             ''', books_list)
    # conn.commit()

def select_all(conn, table):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM {table}')
    rows = cur.fetchall()
    
    if len(rows) == 0:
        print('Not found.')

    return rows

def select_book_by_genre(conn, genre):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM books where genre=?', (genre,))
    rows = cur.fetchall()
    
    return rows

def select_book_by_key(conn, key, value):
    cur = conn.cursor()
    cur.execute(f'SELECT * FROM books where {key}=?', (value,))
    rows = cur.fetchall()
    
    if len(rows) == 0:
        print('Not found.')
    
    return rows

def select_where(conn, table, **query):
    
    
    cur = conn.cursor()

    qs = []
    values = ()

    for key, value in query.items():
        qs.append(f"{key} = ?")
        values += (value,)
    
    q = " AND ".join(qs)

    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()
    
    if len(rows) == 0:
        print('Not found.')

    return rows

def update(conn, table, id, **kwargs):
    
    parameters = [f"{kwarg} = ?" for kwarg in kwargs]
    parameters = ", ".join(parameters)

    values = tuple(value for value in kwargs.values())
    values += (id, )

    sql = f"""
            UPDATE {table}
            SET {parameters}
            WHERE id = ?
            """
    try:
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()
        print('OK')
    except sqlite3.OperationalError as er:
        print('SQLite error: %s' % (' '.join(er.args)))

def delete_where(conn, table, **query):

    qs = []
    values = tuple()

    for key, value in query.items():
        qs.append(f"{key} = ?")
        values += (value,)
    
    q = " AND ".join(qs)

    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table} WHERE {q}", values)
    conn.commit()
    
    print('Deleted.')

def delete_all(conn, table):

    cur = conn.cursor()
    cur.execute(f"DELETE FROM {table}")
    conn.commit()
    
    print('Deleted.')