# Todo basis

import file
import os
import utils
from prettytable import PrettyTable


# path = "~/Documents/programacion/python/gandalf/test"
path = "/home/camilo/todos"

# Add a new todo
def add(filename: str, msg: str) -> None:
    data: str = ""
    if file.exist(path, f"{filename}.txt"):
        data: str = file.read(f"{path}/{filename}.txt")
    file.write(f"{path}/{filename}.txt", f"{data}[ ] - {msg}\n")

    utils.Print("Sucess!", "#DE8F78")


# Remove a todo
def remove(filename: str, linenumber: int):
    lines = file.lines(f"{path}/{filename}.txt")
    del lines[int(linenumber) - 1]
    msg = ""
    for line in lines:
        msg += f"{line}\n"
    file.write(f"{path}/{filename}.txt", msg)


# Update a todo
def update(filename: str, linenumber: int) -> str:
    filepath = f"{path}/{filename}.txt"
    lines = file.lines(filepath)
    prefix = lines[int(linenumber) - 1]
    if prefix[0:3] == "[ ]":
        prefix = f"[x]{prefix[3:]}"
    else:
        prefix = f"[ ]{prefix[3:]}"
    del lines[int(linenumber) - 1]
    lines.append(prefix)
    msg = ""
    for line in lines:
        msg += line
    file.write(filepath, msg)
    utils.Print("Updated!", "green")


# Get a todo
def get(filename: str) -> None:
    data: str = file.read(f"{path}/{filename}.txt")
    utils.Print(f" {filename}.txt", "#6791C9")
    utils.Print(data, "#78b892")


# Get ammount of todos
def size() -> None:
    todofiles = os.listdir(path)
    todosize: int = 0
    for todo in todofiles:
        lines = file.lines(f"{path}/{todo}")
        for line in lines:
            if line[0:3] != "[x]":
                todosize += 1

    print(todosize)


# Return all todos
def all() -> None:
    todofiles = os.listdir(path)
    for todofile in todofiles:
        utils.Print(f" {todofile}", "#6791C9")
        utils.Print(file.read(f"{path}/{todofile}"), "#78B892")


# FIX: this function nedd a refactor
# Format print for init shell
def Table() -> None:
    table = []
    data = []
    dirs = file.alldir(path)
    for dir in dirs:
        content = file.read(f"{path}/{dir}")
        data.append(content if utils.isEmpty(content) else "Nothing")
    table.append(dirs)
    table.append(data)
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])
    tab.align = "l"
    print(tab)
