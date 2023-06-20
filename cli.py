from functions import get_todos, write_todos
import time


todos = get_todos()
now = time.strftime("%b %d,%Y %H:%M:%S")

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]
        todos.append(todo+'\n')

        write_todos(todos)

    elif user_action.startswith('show'):
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}. {item.capitalize()}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            num = int(user_action[5:])
            num = num - 1
            print("To what you want to change " + todos[num].strip('\n') + "?")
            todos[num] = input("Enter new To-Do: ") + '\n'

            write_todos(todos)
        except ValueError:
            print("Wrong command")
            continue
        except IndexError:
            print("Number doesn't exist")
            continue

    elif user_action.startswith('complete'):
        try:
            num = int(user_action[9:])
            index = num -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("There is no such todo")

    elif user_action.startswith('exit'):
        print('Bye')
        break
    else:
        print("Not a valid command")
