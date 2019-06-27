# The Baby CS Bro Guide

<sup></sup>

## How To Use This

### Don't Wanna Git It? No Problem! 

0. [Download this repo as a .zip](https://github.com/rachel-ng/dionysus/archive/master.zip)
1. Proceed with the Normal Steps (skipping 0)

### Let's Git It

You'll be doing stuff in Terminal, so please open it. 

0. Clone this repo into whatever folder you want. If you want it in a folder inside `Documents/` (or whatever other folder you want it to be in) navigate to `Documents/` by doing the following: 
    ```
    $ cd Documents/
    ```
    
    Now you can clone your repo by doing the following:  
    
    ```
    $ git clone git@github.com:rachel-ng/dionysus.git 
    ```
    <sup>If you want to change the folder name to something like `dogs`, just add a space then `dogs` after the clone link</sup>


1. Open the folder

    ```
    $ cd dionysus
    ```
    
    <sup>Or whatever you named the folder</sup>
    
    
2. Create a virtual environment

    ```
    $ python3 -m venv venv_name  
    ```
    
    <sup>I'll be using just `venv` in the code blocks from now on</sup>
    
    Then activate your virtual environment and upgrade `pip`  

    ```
    $ . path/to/venv/bin/activate    # for Linux / OS
    
    (venv) $ pip install --upgrade pip
    ```

3. Install the [dependencies](#dependencies) with [requirements.txt](requirements.txt) by running the following command  
    <sup>It includes Flask, Wheel, *the stuff we use to keep your password safe*, and all that other good stuff!!</sup>

    ```
    (venv) $ pip install -r requirements.txt
    ```
    
    If you don't want to use the [requirements.txt](requirements.txt), you can pretty much just run the following for now: 
    
    ```
    (venv) $ pip3 install wheel
    (venv) $ pip3 install flask
    (venv) $ pip3 install passlib
    ```

4. This is the hard part. You get to edit it however you want. 

5. Now you can run the python file (starting the Flask server)

    ```
    (venv) $ python app.py
    ```

6. Now type one of these into your browser of choice and start using your website!  
<sup>or copy and paste</sup>

    ```
    http://127.0.0.1:5000/
    http://localhost:5000/
    ```

