# список и функция

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [10, 12, 13, 14, 15, 16, 17, 18, 19]


def fun_1 (massiv):
    new_list = []
    for i in massiv:
        if i % 2 == 0:
            new_list += [i]
    print(new_list)

fun_1(list_1)
fun_1(list_2)