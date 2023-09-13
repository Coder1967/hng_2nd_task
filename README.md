# HNG 2ND TASK

# Table of contents
[Installation](#Installation)<br/>
[Usage](#Usage)<br/>
[Dependencies](#Dependencies)<br/>

  
## Installation
```
git clone https://github.com/Coder1967/hng_2nd_task/
```
## Usage
### To run the server
```
hng_2nd_task $ export MYSQL_USER=<user> MYSQL_PWD=<password> MYSQL_HOST=<host>  MYSQL_DB=<datatbase>

hng_2nd_task$ python3 -m api.app
```
## Note: for the following examples, First line shows request and the second line shows expected response
### To add a new user(POST)
```
$ curl -X POST -H "Content-Type: application/json" -d '{"name": "frank"}' http://host:5000/api
$ {"name": "frank", "id": 1}
```
### To update a saved user(PUT)
```
$ curl -X PUT -H "Content-Type: application/json" -d '{"name": "jotaro"}' http://host:5000/api/1
$ {"name": "jotaro", "id": 1}
```
### To delete a saved user(DELETE)
```
$ curl -X DELETE -H http://host:5000/api/1
$ {}
```

### To get a saved user(GET)
```
// With the 'GET' verb, either name or id can be used to read a user
// using id gives you back a single using with the id
$ curl http://host:5000/api/1
$ {"name": "frank", "id": 1}

// using name returns a list if multiple users bear the name and returns a single object
// if only a single user bears it
// e.g if only a user has that name
$ curl http://host:5000/api/frank
$ {"name": "frank", "id": 1}

// if multiple users bear that name
$ curl http://host:5000/api/frank
$ [{"name": "frank", "id": 1}, {"name": "frank", "id": 2}]
```

## Dependencies
```
blinker==1.6.2
cffi==1.15.1
click==8.1.7
cryptography==41.0.3
flask==2.3.3
Flask-Cors==4.0.0
greenlet==2.0.2
importlib-metadata==6.8.0
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
pycparser==2.21
PyMySQL==1.1.0
SQLAlchemy==2.0.20
typing-extensions==4.7.1
werkzeug==2.3.7
zipp==3.16.2
```
