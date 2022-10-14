import copy
from pprint import pprint as print


n=0
def plus_n():
    global n
    n += 1
    return n
# print(n)
xy=[[plus_n() for _ in range(4)]for _ in range(4)]
print(xy,width=20)


def flip_xy(xy):
    flipped = copy.deepcopy(xy)
    for x in range(len(xy)):
        for y in range(len(xy)):
            flipped[y][x]=xy[x][y]
    return flipped

print(flip_xy(xy),width=20)
