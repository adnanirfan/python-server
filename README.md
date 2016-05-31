# Python Sample Server

Files required by Heroku for Python:
1. Web.py(Main file which starts server)
2. runtime.txt
3. requirements.txt
4. Procfile


## 1. web.py
Web Server code written with Flask Framework


## 2. runtime.txt
Define the version of python.
python-2.7.11
or
python-3.5.1


## 3. requirements.txt
To define application dependencies.
<DEPENDENCY_NAME>==<VERSION>
e.g:
Flask==0.10.1


## 4. Procfile
To define the type of process on which our application will run.
