4. from datetime import date

def greet(name):

    return f"Hello, {name}!"

def get_version():

    return "Version: 1.0.0 | Build date: 2026-03-02"

if __name__ == "__main__":

    print(get_version())

    print(greet("Student"))
