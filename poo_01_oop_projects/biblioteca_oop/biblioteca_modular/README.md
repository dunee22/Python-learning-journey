# Library Management System - OOP Modular Project

## Project Overview

This project is a console-based library management system built with Python using Object-Oriented Programming.

The goal of this project is to practice classes, inheritance, composition, methods, object interaction, input validation, menus, and modular project organization.

## Features

* Register new users
* Add new books
* Show all books
* Show all registered users
* Borrow books
* Return books
* Show borrowed books by user
* Validate invalid inputs
* Organize the project into multiple Python modules

## Concepts Practiced

* Object-Oriented Programming
* Classes and objects
* Inheritance
* Composition
* Methods
* Lists of objects
* Input validation
* Menu-driven console applications
* Python modules and imports
* Basic project structure

## Project Structure

```text
biblioteca_modular/
├── main.py
├── persona.py
├── usuario.py
├── bibliotecario.py
├── libro.py
├── biblioteca.py
└── README.md
```

## Files Description

### `main.py`

Main file used to run the program. It contains the interactive menu and helper functions.

### `persona.py`

Contains the `Persona` class, which works as a base class for people in the system.

### `usuario.py`

Contains the `Usuario` class. Users can borrow books, return books, and view their borrowed books.

### `bibliotecario.py`

Contains the `Bibliotecario` class, which inherits from `Persona`.

### `libro.py`

Contains the `Libro` class. Each book has a title, author, and availability status.

### `biblioteca.py`

Contains the `Biblioteca` class. This class manages users, books, borrowing, and returning operations.

## How to Run

Open a terminal inside the `biblioteca_modular` folder and run:

```bash
python main.py
```

## Menu Options

```text
1- Register user
2- Add new book
3- Show books
4- Show users
5- Borrow book
6- Return book
7- Show borrowed books by user
8- Exit
```

## Learning Outcome

This project helped me understand how multiple objects can interact in a real application. It also helped me practice separating code into modules instead of keeping everything in one large file.

This is part of my learning path toward Python, data analysis, and building stronger programming foundations.
