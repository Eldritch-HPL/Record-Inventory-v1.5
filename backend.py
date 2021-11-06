import sqlite3

def connect():
    record=sqlite3.connect("records.db")
    stylus=record.cursor()
    stylus.execute("CREATE TABLE IF NOT EXISTS record (id INTEGER PRIMARY KEY, album text, artist text, year integer, genre text)")
    record.commit()
    record.close()

def insert(album, artist, year, genre):
    record=sqlite3.connect("records.db")
    stylus=record.cursor()
    stylus.execute("INSERT INTO record VALUES (NULL,?,?,?,?)", (album, artist, year, genre))
    record.commit()
    record.close()

def view():
    record=sqlite3.connect("records.db")
    stylus=record.cursor()
    stylus.execute("SELECT * FROM record")
    track=stylus.fetchall()
    record.close()
    return track

def search(album="", artist="", year="", genre=""):
    record=sqlite3.connect("records.db")
    stylus=record.cursor()
    stylus.execute("SELECT * FROM record WHERE album=? OR artist=? OR year=? OR genre=?", (album, artist, year, genre))
    track=stylus.fetchall()
    record.close()
    return track

def delete(id):
    record=sqlite3.connect("records.db")
    stylus=record.cursor()
    stylus.execute("DELETE FROM record WHERE id=?",(id,))
    record.commit()
    record.close()

def update(id, album, artist, year, genre):
    record=sqlite3.connect("records.db")
    stylus=record.cursor()
    stylus.execute("UPDATE record SET album=?, artist=?, year=?, genre=? WHERE id=?",(album, artist, year, genre, id))
    record.commit()
    record.close()

connect()

