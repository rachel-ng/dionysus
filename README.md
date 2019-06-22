# flask_starter

A super basic flask starter kit made based off my work from my [softdev2 final project](https://github.com/tfabiha/ccereal/)  
<sup>so i can live my best lazy life</sup>

For a list of features, refer to [this](#the-good-)

## Usage

### requirements.txt

0. PRE-REQ: You need to be in your virtual environment (venv).  
<sup>Follow the [instructions below](#dependencies) if you don't have a virtual environment</sup>

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


## How to Run

0. Clone this repo into your folder of choice 

    ```
    $ git clone git@github.com:user-name/repo-name.git
    ```

1. Now open your folder

    ```
    $ cd repo-name
    ```

2. Activate your virtual environment and upgrade `pip`  
<sup>Need a virtual environment? Follow the [instructions below](#dependencies)</sup>  

    ```
    $ . path/to/venv/bin/activate    # for Linux / OS
    $ source path/to/venv/Scripts/activate    # for Windows
    
    (venv) $ pip install --upgrade pip
    ```

3. Install the [dependencies](#dependencies) with [requirements.txt](requirements.txt) by running the following command  
<sup>It includes Flask, Wheel, *the stuff we use to keep your password safe*, and all that other good stuff!!</sup>

    ```
    (venv) $ pip install -r requirements.txt
    ```

4. Now you can run the python file (starting the Flask server)

    ```
    (venv) $ python app.py
    ```

5. Now type one of these into your browser of choice and start using your website!  
<sup>or copy and paste</sup>

    ```
    http://127.0.0.1:5000/
    http://localhost:5000/
    ```


## Dependencies

Install the dependencies with [requirements.txt](requirements.txt) by running the following command

```
(venv) $ pip install -r requirements.txt
```

- venv  
`venv` is used to create an isolated environment for whatever version of Python (and whatever libraries you're installing) you're using to wreak havoc in. `venv` allows you to use different versions of Python so you don't need to worry about compatibility issues or somehow breaking your computer.  
`venv` is a standard Python library in Python 3 with no further action required. Run the following to make a virtual environment if you do not already have one: 

    ```
    $ python3 -m venv venv_name 
    ```
    
    For versions older than Python 3.0.0 run the following:  
    ```
    $ pip install virtualenv
    $ virtualenv venv_name  
    ```

- pip  
`pip` is used to install and manage Python packages. Usually comes installed with Python, check out [this page for instructions](https://pip.pypa.io/en/stable/installing/) if you find that further action is required. Remember to upgrade! 

    ```
    (venv) $ pip install --upgrade pip
    ```

- os  
`os` is used for miscellaneous operating system dependent functions. A standard Python library with no further action required.

- sqlite3  
`sqlite3` is used for databases. A standard Python library with no further action required. 

- random
`random` is used to generate random numbers / letters / symbols. A standard Python library with no further action required. 

- urllib  
`urllib` is used to get JSON files from APIs. A standard Python library with no further action required. 

- json  
`json` is used to parse JSON files requested from APIs. A standard Python library with no further action required. 

- flask
`flask` allows the app to be run on `localhost`, needs `wheel`. Installed with [requirements.txt](requirements.txt) 

    ```
    (venv) $ pip3 install flask
    ```

- wheel  
`wheel` is needed to use `flask`. Installed with [requirements.txt](requirements.txt) 

    ```
    (venv) $ pip3 install wheel
    ```

- Jinja2
`Jinja2` is used for templating HTML pages. Installed with [requirements.txt](requirements.txt), installed when you install `flask`

- passlib  
`passlib` is used to hash your password. Installed with [requirements.txt](requirements.txt) 

    ```
    (venv) $ pip install passlib
    ```

## The Good $#!+
- python3
- [flask](http://flask.pocoo.org/)
    - [flash](http://flask.pocoo.org/docs/1.0/patterns/flashing/) `categories`  
      e.g. `flash("Error: Invalid Location", category="location")`  
      <sub>Refer to [lines 62-86](https://github.com/rachel-ng/flask_starter/blob/master/templates/base.html#L62-L86) of [base.html](templates/base.html) for more details</sub>
- [jinja2](http://jinja.pocoo.org/) (for templating)
- [sqlite](https://docs.python.org/3.4/library/sqlite3.html) (DBs, for python functions see [config.py](util/config.py) and [db.py](util/db.py))  
    [config.py](util/config.py) uses `os` for absolute paths  
    <sup>so it doesn't go to absolute hell when you try to make it compatible with apache or something smh 😒</sup>  
    `config.create_table()` has an optional parameter for the table name, defaults to `user`
- accounts
    - stored in [data.db](data/data.db)
    - [db.py](util/db.py): functions for account creation and authentication
    - login, signup, logout (via sessions, POST)
    - password hashing (via `passlib`, uses `sha256_crypt`)
- [bootstrap](https://getbootstrap.com/)
- custom css and js  
    <sup>js file is empty</sup>  
    ```
    static/css/base.css
    <link rel="stylesheet" href="{{ url_for('static', filename='css/base.css') }}">
    ```
    ```
    static/js/my.js
    <script src="{{ url_for('static', filename='js/my.js') }}"></script>
    ```
