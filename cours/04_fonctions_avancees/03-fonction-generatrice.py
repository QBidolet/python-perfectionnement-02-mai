def carres(n):
    i = 1
    while i <= n:
        yield i * i
        i += 1

# for carre in carres(5):
#     print(carre)

iterateur = iter(carres(5))
print(next(iterateur))
print(next(iterateur))
print(next(iterateur))
print(next(iterateur))