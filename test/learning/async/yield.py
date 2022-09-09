def func1():
    yield 1.1
    yield from func2()

def func2():
    yield 2.1
    yield 2.2

f1 = func1()
for item in f1:
    print(item)