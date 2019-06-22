# dionysus

a super basic flask starter kit made based off work from my [softdev2 final project (catatonic cereal)](https://github.com/tfabiha/ccereal/) and the [readme](https://github.com/rachel-ng/group-d-etat) from my [softdev1 final project (ambrosia)](https://github.com/rachel-ng/group-d-etat)  
<sub>so i can live my best life</sub>


## Features (aka *The Good $#!+™*)

- python3, html, css, etc. 
- [.gitignore](.gitignore) (it's also a [gist](https://gist.github.com/rachel-ng/7e26de56cb4a6370164213bd33c31f54))
- [flask](http://flask.pocoo.org/)!)
    - [flash](http://flask.pocoo.org/docs/1.0/patterns/flashing/) `categories`  
      e.g. `flash("Error: Invalid Location", category="location")`  
      <sub>Refer to [lines 62-86](https://github.com/rachel-ng/dionysus/blob/master/templates/base.html#L62-L86) of [base.html](templates/base.html) for more details on implementation</sub>
- [jinja2](http://jinja.pocoo.org/) (for templating)
- [sqlite](https://docs.python.org/3.4/library/sqlite3.html) (DBs, for python functions see [config.py](util/config.py) and [db.py](util/db.py))  
    [config.py](util/config.py) uses `os` for absolute paths  
    <sup>so it doesn't go to *absolute hell* when you try to make it compatible with apache or something</sup>  
    `config.create_table()` has an optional parameter for the table name, defaults to `user`
- accounts
    - stored in [data.db](data/data.db)
    - [db.py](util/db.py): functions for account creation and authentication
    - login, signup, logout (via sessions, POST)
    - password hashing (via `passlib`, uses `sha256_crypt`)
- [bootstrap](https://getbootstrap.com/)
- custom css and js  
    <sup>js file is empty btw</sup>  
    ```
    static/css/base.css
    
    <link rel="stylesheet" href="{{ url_for('static', filename='css/base.css') }}">
    ```
    ```
    static/js/my.js
    
    <script src="{{ url_for('static', filename='js/my.js') }}"></script>
    ```


## Usage

attain the files somehow (fork, download, clone repo and move files, idk it's up to you) and alter them to your choosing

### Important Files

For a full list of features, refer to [the above](#the-good-)

- sample [README.md](sample.md)
- `util/config.py` contains functions for configuring your database  
    you may choose to change the [directory](https://github.com/rachel-ng/dionysus/blob/master/util/config.py#L8) your database is in ( `data/` ) and/or the [db file's name](https://github.com/rachel-ng/dionysus/blob/master/util/config.py#L9) ( `data/data.db` )
- `util/db.py` contains functions for account creation and authentication
- `templates/base.html` the og jinja base html


### requirements.txt

0. PRE-REQ: You need to be in your virtual environment (venv).  
<sup>Follow the [instructions here](sample.md#dependencies) if you don't have a virtual environment</sup>

1. In the root of your repo, run this: 

    ```
    (venv) $ pip freeze > requirements.txt
    ```
    
    This takes a "snapshot" of all your python packages and versions installed within your virtual environment and lists them in your [requirements.txt](requirements.txt) and allows users to run your program on their own computer without worrying about compatibility issues. 
    
2. You can now use your requirements.txt by running the following command: 
    ```
    (venv) $ pip install -r requirements.txt
    ```


### README.md

- [Github's guide](https://guides.github.com/features/mastering-markdown/) to Github flavored markdown
- [adam-p](https://github.com/adam-p)'s [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
