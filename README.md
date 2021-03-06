# AirBnB clone - The console
<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/console.gif" class="responsive"/>

## Description
In this repository we develop the first step in the construction of our first complete web application: the AirBnB clone, which consists in the creation of a custom command interpreter that allows us to manage and store AirBnB objects. This first step is very important because it will help us develop the next steps in which we will implement: HTML / CSS templates, database storage, API, front-end integration ...
<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/first_step_o.png" class="responsive"/>
**This project is part of the Holberton School Full-Stack Software Engineer program.**

## Execution
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

## Usage
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

## Example
<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/canva_video.gif" class="responsive"/>

## Content
| Filename | Description |
| ---- | ---- |
| AUTHORS | List all individuals having contributed content to the repository. Docker's format reference |
| LICENSE | MIT LICENSE AND COPYTIGHT NOTICE |
| console.py | Contains the entry point of the command interpreter `./console.py`|
| base_model.py | Defines all common attributes/methods - contains BaseModel class, constructor and methods |
| `__init__.py` | File to convert directories into python modules, one of them contains reload method from FileStorage class |
| file_storage.py | Serializes/deserializes into JSON/PYTHON format - contains FileStorage class and methods |
| user.py | Inherits from BaseModel - contains class attributes like email, password, first_name and last_name |
| state.py | Inherits from BaseModel - contains class attributes like name |
| city.py | Inherits from BaseModel - contains class attributes like state_id and name |
| amenity.py | Inherits from BaseModel - contains class attributes like state_id and name |
| place.py | Inherits from BaseModel - contains class attributes like city_id, user_id, name, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude and amenity_ids |
| review.py | Inherits from BaseModel - contains class attributes like place_id, user_id and text |
| README.md | Description of the proyect and command interpreter |

## BaseModel Methods
| Class | Methods |
| ---- | ---- |
| `__str__()` | returns string format of the object, with class.name id and dict |
| save() | updates instance attribute updated_at and save string into file.json |
| to_dict() | returns a dictionary with isoformat, class name and all keys/values |

## FileStorage Methods
| Class | Methods |
| ---- | ---- |
| all() | returns a dictionary `__objects` |
| new() | sets the argument given as a value in the dictionary |
| save() | serializes from string to json and store it in file.json |
| reload() | deserializes from json to string and store it in file.json using save |

## Tests
- The code of this project is tested with the **unittest** module, to run it type:
```python
$ python3 -m unittest discover tests
```

<img src="https://github.com/AlisonQuinter17/AirBnB_clone/blob/main/multimedia/logos.png" class="responsive"/>

## Environment
* Language: Python3
* OS: Ubuntu 14.04 LTS
* Style guide for Python code: [PEP8](https://www.python.org/dev/peps/pep-0008/)

## Authors
* [Alison Quintero](https://twitter.com/AlisonQuinter17)
* [Andres Ariza](https://twitter.com/ariza_rocks)
