import copy
import itertools
from pprint import pprint
import random

shape_n = 5
shapes = [[''.join([str(random.randint(0, 1)) for i in range(shape_n)])
           for i in range(shape_n)] for i in range(shape_n)]
# pprint(shapes)

shapes1 = [["000", "110", "000"], ["110", "011", "000"], ["110", "011", "110"], [
    "000", "010", "111"], ["011", "111", "011"], ["011", "010", "000"]]


# 判断 中间(n-2)*(n-2) 是否都为1


def if_mid_is_all_1(shapes):
    for single_pane in shapes:
        single_pane_mid_strs = single_pane[1:][:-1]
        # print(single_pane_mid_strs)
        for single_numbers in single_pane_mid_strs:
            mid_numbers = single_numbers[1:][:-1]
            if "0" in mid_numbers:
                return 0
    return 1


# print("中间是否都是1:",if_mid_is_all_1(shapes1))


# 判断 所有1是否都相连通
def all_1_is_connected(shapes):
    shape_n = len(shapes[0])
    for single_index, single_pane in enumerate(shapes):
        # 面
        for i, listi in enumerate(single_pane):
            # 行
            for j, valuej in enumerate(listi):
                # 字
                if valuej == "1":
                    around_list = [
                        shapes[single_index][i][j+1] if j +
                        1 < shape_n else 0,
                        (shapes[single_index][i][j-1]) if j-1 >= 0 else 0,
                        (shapes[single_index][i-1][j]) if i-1 >= 0 else 0,
                        (shapes[single_index][i+1][j]) if i +
                        1 < shape_n else 0,
                    ]
                    # print(around_list)
                    if "1" not in around_list:
                        print(single_index, i, j)
                        return 0
    return 1


# print("所有1是否相连接:", all_1_is_connected(shapes1))

def reverse(pane):

    reversed_pane = copy.deepcopy(pane[::-1])
    for row, row_line in enumerate(reversed_pane):
        reversed_pane[row] = row_line[::-1]

    return reversed_pane

# print(reverse(pane))


def rotate_pane(pane):
    pane_yx = [''.join([pane[row][col] for row in range(len(pane))])
               for col in range(len(pane))]
    pane90 = pane_yx[::-1]
    pane180 = reverse(pane)
    pane270 = reverse(pane90)
    rotated_pane = [pane, pane90, pane180, pane270]
    return rotated_pane

# pane_random=shapes[0]
# print(pane_random)
# print(rotate_pane(pane_random))


def rotate_shape(shape):
    rotated_shape = []
    for pane in shape:
        rotated_shape.append(rotate_pane(pane))
    return rotated_shape


# pprint(rotate_shape(shapes1))

def all_shape(shape):
    all_shape_list = []
    [A, B, C, D, E, F] = shape
    # print(A)
    for a in rotate_pane(A):
        for b in rotate_pane(B):
            for c in rotate_pane(C):
                for d in rotate_pane(D):
                    for e in rotate_pane(E):
                        for f in rotate_pane(F):
                            listx = [a, b, c, d, e, f]
                            listx_permuted = list(itertools.permutations(listx))
                            all_shape_list += listx_permuted
    return all_shape_list


# pprint(list(itertools.permutations(shapes1)))
pprint(len(all_shape(shapes1)))

# shape_one=[0 for i in range(6)]
# rotated_shape = rotate_shape(shape)
# for index, pane in enumerate(rotated_shape):
#     for surface in pane:
#         shape_one[index]=surface


def one_cube_is_ok(shape):
    n = 3
    cube = [[[0 for i in range(n)] for i in range(n)]for i in range(n)]
    # pprint(cube)
    cube_n = len(cube)
    fail = 0
    if_mid_is_all_1(shapes)

    def check_pane(pane_incube, pane_inshape):
        if int(pane_incube) == int(pane_inshape) == 1:
            fail = 1
        pane_incube = 1 if int(pane_incube) != int(pane_inshape) else 0

    for z in range(cube_n):
        for y in range(cube_n):
            for x in range(cube_n):

                # 分别检测每一面
                if z == 0:
                    cube[0][y][x] = shape[0][y][x]
                if y == 0:
                    check_pane(cube[z][0][x], shape[1][z][x])
                if x == 0:
                    check_pane(cube[z][y][0], shape[2][z][y])
                if z == n-1:
                    check_pane(cube[n-1][y][x], shape[3][y][x])
                if y == n-1:
                    check_pane(cube[z][n-1][x], shape[4][z][x])
                if x == n-1:
                    check_pane(cube[z][y][n-1], shape[5][z][y])

                # 中间的数值赋值
                if x not in [0, n-1] and (y not in [0, n-1]) and (z not in [0, n-1]):
                    cube[z][y][x] = 1
    # pprint(cube)
    for z in cube:
        for y in z:
            if 0 in y:
                return 0

    return 1
# print(one_cube_is_ok(shapes1))


def check_all_cube_is_ok(shape):
    if all_1_is_connected(shape) == 0:
        return 0
    if if_mid_is_all_1(shape) == 0:
        return 0
    all_shape_list = all_shape(shape)
    for one_shape in all_shape_list:
        if one_cube_is_ok(one_shape) == 1:
            return 1
    return 0

print(check_all_cube_is_ok(shapes1))
