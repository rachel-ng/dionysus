import os, sqlite3
from passlib.hash import sha256_crypt # password hashing -- sha256_crypt.hash(hash_this)

from util import config

config.create_table()

def add_user(username, password):
    '''
    was this user added to TABLE users? 
    '''
    db, c = config.start_db()
    data = c.execute("SELECT * FROM users;")
    for row in data: # is this username available
        if username == row[1]: 
            config.end_db(db)
            return False
    command = "INSERT INTO users (username,password) VALUES (?,?);"
    c.execute(command,(username,sha256_crypt.hash(password)))
    config.end_db(db)
    return True

# rEwRiTe THiS adsfkhjkadsfhkadhskl 
def auth_user(username, password):
    db, c = config.start_db()
    #data = c.execute("SELECT * FROM users;")
    command = "SELECT password FROM users WHERE username = ?;"
    c.execute(command,(username,))
    pw = c.fetchone()[0]
    if sha256_crypt.verify(password, pw): 
       config.end_db(db)
       return True
    #for row in data:
    #    if row[0] == username and sha256_crypt.verify(password, row[1]):
    #        config.end_db(db)
    #        return True
    config.end_db(db)
    return False

def registered(username):
    '''
    is this username available? 
    '''
    db, c = config.start_db()
    command = "SELECT * FROM users;"
    c.execute(command)
    data = c.fetchall()
    print(data)
    for row in data:
        if username == row[0]:
            config.end_db(db)
            return False
    config.end_db(db)
    return True

def all_users():
    '''
    returns a dictionary with usernames + hashes passwords
    '''
    db, c = config.start_db()
    command = "SELECT username, password FROM users;"
    c.execute(command)
    all_users = c.fetchall()
    config.end_db(db)
    users = {}
    for item in all_users:
        users[item[0]] = item[1]
    return users
