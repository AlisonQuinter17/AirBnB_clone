# AirBnB clone - The console
<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/console.gif" class="responsive"/>

## Description
In this repository we develop the first step in the construction of our first complete web application: the AirBnB clone, which consists in the creation of a custom command interpreter that allows us to manage and store AirBnB objects. This first step is very important because it will help us develop the next steps in which we will implement: HTML / CSS templates, database storage, API, front-end integration ...
<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/first_step_o.png" class="responsive"/>
**This project is part of the Holberton School Full-Stack Software Engineer program.**

## Usage
- You can run the console mode:
### Interactive
```python
$ ./console.py
(hbnb)
```
### Non-Interactive
```python
$ echo "help" | ./console.py
(hbnb)
```
## Example

<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/canva_video.gif" class="responsive"/>

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

## Tests
- The code of this project is tested with the **unittest** module, to run it type:
```python
$ python3 -m unittest discover tests
```
## What is inside
| File | Description |
| ---- | ---- |
| README.md | Description of the proyect and command interpreter |
| AUTHORS | List all individuals having contributed content to the repository. Docker's format reference |
| LICENSE | MIT LICENSE AND COPYTIGHT NOTICE |
| console.py | Contains the entry point of the command interpreter `./console.py`|
| base_model.py | Defines all common attributes/methods - contains BaseModel class, constructor and methods |
| `__init__.py` | File to convert directories into python modules, one of them contains reload method from FileStorage class |
| file_storage.py | Serializes/deserializes into JSON/PYTHON format - contains FileStorage class and methods |
| user.py | Inherits from BaseModel - contains class attributes like email, password, first_name and last_name |
| state.py | Inherits from BaseModel - contains class attributes like name |
## Environment
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guide for Python code: [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Authors
* [Alison Quintero](https://twitter.com/AlisonQuinter17)
* [Andres Ariza](https://twitter.com/ariza_rocks)
