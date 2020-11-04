# AirBnB clone - The console
<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/console.gif" class="responsive"/>

## Description
In this repository we develop the first step in the construction of our first complete web application: the AirBnB clone, which consists in the creation of a custom command interpreter that allows us to manage and store AirBnB objects.

This first step is very important because it will help us develop the next steps in which we will implement: HTML / CSS templates, database storage, API, front-end integration ...

**This project is part of the Holberton School Full-Stack Software Engineer program.**

## Usage
- To run the console you must run the console.py file:
```python
./console.py
(hbnb)
```

| Command  |  Description  | Use |
| ----- | ----- | ----- |
| create |Create an instance (object) and print its id.| **(hbnb)** create `<class>` |
| show |Prints the string representation of an instance based on the class name and id.| **(hbnb)** show `<class>` `<id>` |
| destroy | Deletes an instance based on the class name and id | **(hbnb)** destroy `<class>` `<id>` |
| all | Prints all string representation of all instances based or not on the class name. |**(hbnb)** all `<class>` *or*  **(hbnb)** all|
| update | Updates an instance based on the class name and id by adding or updating attribute. | **(hbnb)** update `<class>` `<id>` `<attribute name>` `"<attribute value>"` |
| count | Prints the total number of instances of a class. | **(hbnb)** `<class name>`.count() |
| quit / EOF | Exit the program. | **(hbnb)** quit *or* **(hbnb)** EOF |
| help | This action is provided by cmd by default, but should be kept up to date and documented. | **(hbnb)** help |


## Environment
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guide for Python code: [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Authors
* [Alison Quintero](https://twitter.com/AlisonQuinter17)
* [Andres Ariza](https://twitter.com/ariza_rocks)
