def generator():
    for i in range(5):
        yield i

print(type(generator()))
g = generator()
print(next(g))
print(next(g))
print(next(g))

print("-------")

for i in g:
    print(i)

print("-------")

for i in generator():
    print(i)