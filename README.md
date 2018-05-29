# What is GODA?

GODA is a programming language that allows the user to manipulate and administer data. Users can create collections of user-defined objects and keep them in libraries. Users can create, import, and export their own libraries and collections. Users may also import their own custom made commands and apply them to selected libraries.

<html>
<body>
  <div align="center">
<iframe width="720" height="345" src="https://www.youtube.com/watch?v=dzbKYmk1koE">
</iframe>
    </div>
</body>
</html>

# Overview

## Motivation

Managing databases can often be tedious. GODA (Generic Objective Data Administrator) is a command line designed to ease the process of manipulating databases. From a quick deployment to easy-to-learn commands, GODA is aimed towards versatility and flexibility, allowing the users to create, import, and exports their own databases through csv files, and importing their own written algorithms as commands to carry out tasks that would otherwise be impossible with other programs. GODA is an objective data administrator, which means data is interpreted and treated as unique objects with their own attributes. It also allows the user to work on multiple databases at the same time.

## Features

- help - will display a list of all commands available to be used
- help [command] - will display specific description about [command]
- open - will open an existing library
- crt - create a new library, collection, object type, or object instance
- show - display a library, a collection, or a list of all existing libraries
- rm - remove a library, collection, or object instance
- sort - sort a collection by a specific attribute
- merge - merge two collections to create a new collection
- search - search for all object instances with a specific attribute
- imp - import a library, collection, or command
- exp - export a library or collection to Desktop
- run - run an imported command

## Approach

1. GODA uses a lexical analyzer to read user input and a parser to carry out the instructions.
2. GODA.py is the main module which contains the lexical analyzer and the parser.
3. The parser directly communicates with Handler.py which connectes all other modules and ADTs.
4. We used PLY: Python Lexical Yacc


### Documentation

Learn more about GODA and see a reference manual [here](https://drive.google.com/file/d/1ZtkemYuCiujQxlnPhb1pGyt5FayfUukk/view)
