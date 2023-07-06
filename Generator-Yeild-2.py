def create_num():
    yield 1
    yield 2 
    yield 3
    yield 4

generator = create_num()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))