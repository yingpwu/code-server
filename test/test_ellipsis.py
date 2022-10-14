def ellipsis_type():
    print(type(...))
    print(Ellipsis==...)
    print(...)

# ellipsis_type()

def fun1():pass
def fun2():...

def ellipsis_in_np():
    import numpy as np

    # arr=np.random.random((2,2,2))
    # print(arr)
    # print(arr[...,0,0])
    a = np.array([[[1, 2, 21], [3, 4, 34]],
                  [[5, 6, 56], [7, 8, 78]]])
    print("a:", a)
    print('a.shape:', a.shape)
    print("-"*10)

    b = a[..., 0:2]
    print('b :', b)
    print('shape.b:', b.shape)
    print("-"*10)



ellipsis_in_np()
