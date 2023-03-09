
FILEPATH = "../Python/todos.txt"


def read(filename=FILEPATH):
    with open(filename, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write(todos_arg, filename=FILEPATH):
    with open(filename, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")

