a = 'I am global !'

def enclosing_function():
    a = 'I am from enclosed function!'

    def inner_function():
        a = 'I am local!'
        print(a)
    inner_function()

def print_global():
    a = 'I am from enclosed function!'

    def inner_function():
        global a
        print(globals()['a'])
    inner_function()

def print_enclosed():
    a = 'I am from enclosed function!'

    def inner_function():
        nonlocal a
        print(a)
    inner_function()


def main():
    enclosing_function()
    print_global()
    print_enclosed()


if __name__ == '__main__':
    main()