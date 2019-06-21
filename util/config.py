import os, sqlite3

CUR_DIR = os.path.dirname(__file__)  # abs path current directory
ROOT_DIR = os.path.join(CUR_DIR, os.path.pardir)  # root directory
DATA_DIR = os.path.join(ROOT_DIR, 'data')  # data directory

DB_FILE = os.path.join(DATA_DIR, 'data.db')  # db file

def start_db():
    db = sqlite3.connect(DB_FILE)
    c = db.cursor()
    return db, c

def end_db(db):
    db.commit()
    db.close()

def create_table(table_name="user"):
    db, c = start_db()
    command = "CREATE TABLE IF NOT EXISTS ? (username TEXT, password TEXT)"
    c.execute(command,(table_name,))
    end_db(db)
