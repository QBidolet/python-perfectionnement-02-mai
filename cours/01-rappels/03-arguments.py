def ma_fonction(a, b, c):
    pass


# paramètres positionnels
ma_fonction(1, 2, 3)

# keywords arguments
ma_fonction(b=1, c=2, a=3)

# toujours positionnels avant keywords
ma_fonction(1, c=3, b=2)


# interdit
# ma_fonction(c=3, b=2, 1)

def ma_fonction(a, b, c, *args):
    print(args)
    for arg in args:
        print(arg)


ma_fonction(1, 2, 3, 4, 5, 6, 7, 8)


def ma_fonction(a, b, c, **kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, value)


ma_fonction(1, 2, 3, arg_1=12, arg_2=13)


# mélanger args et kwargs
def ma_fonction(*bidule, **machin):
    pass
