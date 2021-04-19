def generator():
    for i in range(5):
        yield i

print(type(generator()))
g = generator()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
