<p align="center">
 <h1 align="center"> AirBnB clone - RESTful API </h1>
 <a href="" rel="noopener">
 <img src="https://github.com/bdbaraban/AirBnB_clone_v2/raw/master/assets/hbnb_logo.png">

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()

</div>

---

<p align="center"> This project aims to develop a command-line interpreter and a RESTful API for managing objects in an AirBnB-like application. The interpreter and API facilitate the creation, storage, retrieval, updating, and deletion of various objects such as users, states, cities, and places.
    <br> 
</p>

## Table of Contents 📝

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)

## About <a name = "about"></a> 🧐

This project presents a command-line interpreter and a RESTful API designed for managing objects within an AirBnB-like application. Users can efficiently create, store, retrieve, update, and delete entities like users, states, cities, and places directly from their terminal or through HTTP requests using the API.

The core of the project is a robust object-oriented structure featuring a parent class (BaseModel) that handles essential functionalities such as initialization and serialization. A streamlined serialization process allows the interpreter to seamlessly convert object instances to dictionaries, JSON strings, and ultimately to files for efficient data storage and retrieval.

### New Feature: DBStorage and RESTful API with Flask

This updated version introduces DBStorage, a new storage mechanism that leverages a MySQL database for persisting application data. By setting the environment variable `HBNB_TYPE_STORAGE=db`, the application utilizes a `DBStorage` instance to interact with the database. This instance connects to the MySQL server using credentials and database information specified in environment variables (`HBNB_MYSQL_USER`, `HBNB_MYSQL_PWD`, `HBNB_MYSQL_HOST`, and `HBNB_MYSQL_DB`).

Additionally, this version integrates a RESTful API built with Flask, allowing external applications and services to interact with the AirBnB clone application programmatically via HTTP methods. The API provides endpoints for all CRUD operations, making it flexible and easy to integrate with front-end frameworks and other tools.

## Getting Started <a name = "getting_started"></a> 🏁

1. Clone the repo



```
$ git clone https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone_v3.git

```

2.run console.py

```
$ ./console.py
```

## Requirements 📃

- Python 3.7+
- Flask
- MySQL
- SQLAlchemy

or run 
```
$ pip install -r requiements.txt
```

## Running the tests <a name = "tests"></a> 🔧

Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:



```
$ python3 unittest -m discover tests
```

Alternatively, you can specify a single test file to run at a time:

```
$ python3 unittest -m tests/test_console.py
```

## Usage of console <a name="usage"></a> 💻

The console is a command line interpreter that permits management of the backend of HolbertonBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

### Using the Console

The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file console.py at the command line.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/help.gif?raw=true)

Alternatively, to use the HolbertonBnB console in interactive mode, run the file console.py by itself:

```
$ ./console.py
```

To quit the console, enter the command quit, or input an EOF signal (ctrl-D).

```
$ ./console.py
(hbnb) quit
$
```

```
$ ./console.py
(hbnb) EOF
$
```

### Console Commands

The HolbertonBnB console supports the following commands:

#### create

- Usage: `create <class>`
  Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file `file.json`

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/create.gif?raw=true)

#### show

- Usage: show `<class> <id>` or `<class>.show(<id>)`
  Prints the string representation of a class instance based on a given id.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/show.gif?raw=true)

#### destroy

- Usage: destroy `<class> <id>` or `<class>.destroy(<id>)`
  Deletes a class instance based on a given id.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/destory.gif?raw=true)

#### all

- Usage: all or all `<class>` or `<class>.all()`
  Prints the string representations of all instances of a given class. If no class name is provided, the command prints all instances of every class.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/all.gif?raw=true)

#### count

- Usage: count `<class>.count()`
  Retrieves the number of instances of a given class.

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/count.gif?raw=true)

#### update

- Usage: update `<class> <id> <attribute name> "<attribute value>"` or `<class name>.update(<id>, <dictionary representation>)`
  Updates a class instance based on a given id with a given key/value attribute pair or dictionary of attribute pairs. If update is called with a single key/value attribute pair, only "simple" attributes can be updated (ie. not id, created_at, and updated_at).

![](https://github.com/VoiceOfDarkness/holbertonschool-AirBnB_clone/blob/main/assets/update.gif?raw=true)

## Authors <a name = "authors"></a> ✍️

- [@VoiceOfDarkness](https://github.com/VoiceOfDarkness)
- [@heydarov93](https://github.com/heydarov93)

### Special Credits:

> You really don't need to know, but here's the link if you're curious:[link](https://www.youtube.com/watch?v=BJ1ctMVMTK0)
