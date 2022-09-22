# main file

import sys
import todo as todo


def main():
    # [1] operation [2] filename [3] content
    operation = sys.argv[1]

    if operation == "add":
        todo.add(sys.argv[2], sys.argv[3])
    elif operation == "remove":
        todo.remove(sys.argv[2], sys.argv[3])
    elif operation == "update":
        todo.update(sys.argv[2], sys.argv[3])
    elif operation == "get":
        todo.get(sys.argv[2])
    elif operation == "size":
        todo.size()
    elif operation == "all":
        todo.all()
    elif operation == "table":
        todo.Table()
    else:
        print(f"{operation} is not a valid argument")


if __name__ == "__main__":
    main()
