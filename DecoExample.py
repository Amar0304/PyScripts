# Example of decorated and generator


def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1


def tes():
    for i in countdown():
        print(i)


def decor(tes):
    def wrap():
        tes()

    return wrap


decorated = decor(tes)
decorated()
