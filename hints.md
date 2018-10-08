# Hints

Here are some hints that might help when working on this lab:

## 1. Getting a SQLite Database set up

```
import sqlite3
connection = sqlite3.connect(filename)
cursor = connection.cursor()
```
* Note that the file doesn't need to exist already. So you could connect("empty.db") and it'd create a new file called empty.db and save changes to the database there. 

## 2. Reading the contents of a text file and saving it to a variable

```
sql = open(filename, "r").read()
```
