FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Get the to-do items from a file. Default parameter is todos.txt"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items from a list to a text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

