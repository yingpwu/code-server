import itertools


a = [4, 5, 6, 7, 3, 3, 21]
print(a.index(min(a)))
n = 0
min_a = min(a)
min_a_index = [index for index, value in enumerate(a) if value == min(a)]
# print(min_a_index)


# list1 = list2 = list3 = []
# print(id(list1))
# print(id(list2))
# print(id(list3))
# list3.append("4")

# print(list1)
# print(list2)
# print(list3)

# list1 = [0, 1, 0]
# list2 = [1, 0, 1]
# list3 = list1 or list2
# list4 = [1 if list1[i] != list2[i] else 0 for i in range(len(list1))]
# print(list3)
# print(list4)
# [A,B,C]=[1,2,3]

# print(A,B,222,C)
list1 = [1, 2, 3]
list2 = [1, 0, 0]
print(list1 == list2)
listx = []
for n1, x1 in enumerate(listx):
    for n2, x2 in enumerate(listx):
        for n3, x3 in enumerate(listx):
            if n1 != n2 and n1 != n3 and n2 != n3:
                listx.append([x1, x2, x3])
# print(listx)
# listy=itertools.permutations(list1,3)
# print(list(listy))
for x in list1:
    