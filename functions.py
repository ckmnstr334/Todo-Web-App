FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of 
    to do items. 
    """ # docsting for documentation of the function and readability by others. triple quotes also enable multiline strings.
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH): #2. ist Pfad, 1. ist Inhalt von writelines
    """ Write to-do items list to a text file. """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)
# 2 breaklines between functions and rest of the code recommended

if __name__ == "__main__":
    print(get_todos())