def fonction_externe(x):
    def fonction_interne(y):
        return x+y

    return fonction_interne

addition_1 = fonction_externe(1)
addition_2 = fonction_externe(2)
print(addition_1(5))
print(addition_2(10))
