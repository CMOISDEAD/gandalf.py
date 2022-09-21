# files utils

import os


# Read the content of a file
def read(filepath: str) -> str:
    with open(filepath, "r") as file:
        return file.read()


# Write a file
def write(filepath: str, msg: str) -> None:
    with open(filepath, "w") as file:
        file.write(msg)


# Delete a file
def delete(filepath: str) -> None:
    os.remove(filepath)


# Check if a file exist
def exist(path: str, filename: str) -> bool:
    for file in os.listdir(path):
        if file == filename:
            return True
    return False


# Return the number of line in a file
def numberlines(filepath: str) -> int:
    number_lines = 0
    with open(filepath) as fp:
        for line in fp:
            if line.strip():
                number_lines += 1
    return number_lines


# Return a list with all lines of a file
def lines(filepath: str) -> list:
    with open(filepath, "r") as file:
        return file.readlines()


# Return a list with all elements in a dir
def alldir(path: str) -> list:
    return os.listdir(path)
