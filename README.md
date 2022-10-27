# AirBnB clone - The console

## Description of the Project

This is the first part of the AirBnB Clone project for Holberton: The objective of this project is to implement a server with a simple copy of the AirBnB web application to demonstrate the understanding and development of front-end and back-end technical skills. .

## The general scope of the project is:

* Create a command line interpreter to manipulate data without a visual interface.

# Description of the Command Interpreter:

The console allows us to create the data model, manage objects, and store and save objects to a file (JSON file). Some examples:

    > Create a new object (ex: a new User or a new Place).
    > Retrieve an object from a file, a database etc…
    > Do operations on objects (count, compute stats, etc…).
    > Update attributes of an object.
    > Destroy an object.

The first part is to manipulate the storage system. This storage engine will give us an abstraction between "Our objects" and "How they are stored and persisted", by means of json files, this means that we will not have to pay attention (care) in how our objects are stored. This abstraction will also allow us to change the storage type easily without updating our entire code base.

The console will be a tool to validate this storage engine.

## How to start it

> """interactive mode"""
> User$ ./console.py 
(hbnb) help

> """non-interactive mode"""
> User$ echo "help" | ./console.py

Documented commands (type help < topic >):
## How to use it


This is the command's list:

    * help - Shows information about the console or its commands - Usage: help or help create
    * EOF - Exits the console
    * quit - Exits the console
    * create - Creates an instance - Usage: create Class
    * show - Prints the string representation of an instance - Usage: show Class id
    * destroy - Deletes an intance - Usage: destroy Class id
    * all - Prints all string representation of all instance - Usage: all or all Class
    * update - Updates an instance - Usage: update Class id attribute value

## Examples

Create:

    > (hbnb) create BaseModel

af9b4cbd-2ce1-4e6e-8259-f578097dd15f

    >(hbnb) create User

40362ad0-4a6d-48b8-98e9-baaaa282e7c6

    >(hbnb) create Place
    >a42ee380-c959-450e-ad29-c840a898cfce

show:

    >(hbnb) show User 2bf3ebfd-a220-49ee-9ae6-b01c75f6f6a4
    >[User] (40362ad0-4a6d-48b8-98e9-baaaa282e7c6) {'id': >'40362ad0-4a6d-48b8-98e9-baaaa282e7c6', 'created_at': datetime.datetime(2022, 10, 27, >12, 58, 30, 918358), 'updated_at': datetime.datetime(2022, 10, 27, 12, 58, 30, 918389)}


