# The Good $#!+
- python3
- [flask](http://flask.pocoo.org/) (routing, flashing, all that good stuff)
- [jinja2](http://jinja.pocoo.org/) (templating)
- [sqlite](https://docs.python.org/3.4/library/sqlite3.html) (DBs, for python functions see [config.py](util/config.py) and [db.py](util/db.py))  
    [config.py](util/config.py) uses `os` for absolute paths  
    <sup>so it doesn't go to absolute hell when you try to make it compatible with apache or something smh 😒</sup>  
    `config.create_table()` has an optional parameter for the table name, defaults to `user`
- accounts
    - stored in [data.db](data/data.db)
    - [db.py](util/db.py): functions for account creation and authentication
    - login, signup, logout (via sessions)
    - password hashing (via `passlib`, uses `sha256_crypt`)
- [bootstrap](https://getbootstrap.com/)
