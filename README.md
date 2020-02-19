# AirBnB Clone: The Console

In an attempt to mimic AirBnB's website and design, this repository consists of code that handles the console. Currently this is the first of many steps towards recreating AirBnB's layout, with the endgoal of having an identical version of AirBnB.

## Description:

* Allows creation of new instances
* Saves and reloads instances to and from JSON
* Allows deleting of instances
* Properly stores instances using a file_storage function
* Handles classes used for AirBnb (ie city, state, place, amenity, review, user)

## Requirements:

* Contain the line #!/usr/bin/python3 as the very first line
* Properly use classes and imports
* Proper documentation of classes and files
* Pass PEP8 style
* Pass unittests

## How to Run and Use the Console:

1. Type "./console.py" (without quotation marks)
2. The prompt "(hbnb) " should appear. From here, enter a command. A list of available commands can be seen by typing help. For further information on a specific command, type help <command>. For example, help create. Note that many commands require arguments to be passed in
3. Depending on the command (and arguments), execute the proper programs
4. Wait for the next command(s) to be entered
5. Repeat step 3 as needed
6. Close the console using either quit or EOF
7. ~~Hotel? Trivago~~

## Files in This Repository:

| File Name | Description|
| --- | --- |
|[console.py](https://github.com/Alouie412/AirBnB_clone/blob/master/console.py) | The console. Run this to enter commands |
|[models/base_model.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/base_model.py) | The BaseModel class and workhorse file of this repository. Handles creating or recreating of instances, saving them, and converting to dictionary |
|[models/amenity.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/amenity.py) | The Amenity class that inherits from BaseModel. Handles anything related to amenities |
|[models/city.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/city.py) | The City class that inherits from BaseModel. Handles anything related to cities |
|[models/place.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/place.py) | The Place class that inherits from BaseModel. Handles anything related to places |
|[models/review.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/review.py) | The Review class that inherits from BaseModel. Handles anything related to reviews |
|[models/state.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/state.py) | The State class that inherits from BaseModel. Handles anything related to states |
|[models/user.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/user.py) | The User class that inherits from BaseModel. Handles anything related to users |
|[models/__init__.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/__init__.py) | The init file that creates unique FileStorage instances to be used and connected to by BaseModel |
|[models/engine/file_storage.py](https://github.com/Alouie412/AirBnB_clone/blob/master/models/engine/file_storage.py) | The FileStorage class and other workhorse file of this repository. Handles filling in the dictionary, saving to JSON, and reloading from JSON |

## Console Commands:

| Command Name | Description |
| --- | --- |
| quit | Exits the console |
| EOF | Exits the console |
| help <command> | Displays all commands. If a command is passed in, displays information about that specific command |
| create <class name> | Creates a new instance. Saves the instance to a JSON file and prints the id |
| show <class name> <id> | Displays information of a specific class name and id |
| destroy <class name> <id> | Removes an instance. The result will be saved to a JSON file |
| all <class name> | Displays all information. If a class name is passed in, displays all information only of that class name |
| update <class name> <id> <attribute name> <attribute value> | Updates an attribute name at a specific class name and id with the attribute value |
  
## Sample Output:
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py
(hbnb) all
(hbnb) all AwesomeClass
** class doesn't exist **
(hbnb) create AwesomeClass
** class doesn't exist **
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseClass
** class doesn't exist **
(hbnb) destroy BaseModel
** instance id missing **
(hbnb) destroy BaseModel 555
** no instance found **
(hbnb) create BaseModel
b8843b85-faa3-41c0-ace5-e17ae45d1e4b
(hbnb) all
["[BaseModel] (b8843b85-faa3-41c0-ace5-e17ae45d1e4b) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766798), 'id': 'b8843b85-faa3-41c0-ace5-e17ae45d1e4b', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766751)}"]
(hbnb) show BaseModel b8843b85-faa3-41c0-ace5-e17ae45d1e4b
[BaseModel] (b8843b85-faa3-41c0-ace5-e17ae45d1e4b) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766798), 'id': 'b8843b85-faa3-41c0-ace5-e17ae45d1e4b', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766751)}
(hbnb) create BaseModel
f3eb800d-2cb4-45a3-8fda-0f12d0c71d63
(hbnb) all
["[BaseModel] (b8843b85-faa3-41c0-ace5-e17ae45d1e4b) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766798), 'id': 'b8843b85-faa3-41c0-ace5-e17ae45d1e4b', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 3, 766751)}", "[BaseModel] (f3eb800d-2cb4-45a3-8fda-0f12d0c71d63) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56543), 'id': 'f3eb800d-2cb4-45a3-8fda-0f12d0c71d63', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56500)}"]
(hbnb) destroy BaseModel b8843b85-faa3-41c0-ace5-e17ae45d1e4b
(hbnb) all
["[BaseModel] (f3eb800d-2cb4-45a3-8fda-0f12d0c71d63) {'updated_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56543), 'id': 'f3eb800d-2cb4-45a3-8fda-0f12d0c71d63', 'created_at': datetime.datetime(2020, 2, 19, 22, 26, 37, 56500)}"]
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help EOF
EOF command to exit the program
(hbnb) quit
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$
```

## Authors

[Anthony Louie](https://github.com/Alouie412)
