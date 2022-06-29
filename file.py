# список и функция

list = [1,2,3,4,5,6,7,8,9]

def fun_1 (massiv):
    new_list = []
    for i in massiv:
        if i > 4:
            new_list += [i]
    print(new_list)

fun_1(list)