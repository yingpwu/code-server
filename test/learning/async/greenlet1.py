from greenlet import greenlet

def func1():
    print(1.1)
    gl2.switch()
    print(1.2)
    gl2.switch()

def func2():
    print(2.1)
    gl1.switch()
    print(2.2)
    gl1.switch()

gl1=greenlet(func1)
gl2=greenlet(func2)

gl1.switch()