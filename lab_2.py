def task_a(names):
    return names


def task_b(int_list):
    # new_list =[]
    # for i in range(len(int_list)):
    # new_list.append(int_list[i] * 2)
    # return new_list

    new_list = [i * 2 for i in int_list]
    return (new_list)


def task_c(list_of_ten_ints):
    new_list = []
    for i in range(len(list_of_ten_ints)):
        if list_of_ten_ints[i] % 2 == 0:
            new_list.append(list_of_ten_ints[i])
    return new_list


def task_d(list_of_ten_ints):
    new_list = []
    for i in range(len(list_of_ten_ints)):
        if i % 2 == 0:
            new_list.append(list_of_ten_ints[i])
    return new_list


if __name__ == '__main__':
    names = ['Asia', 'Ania', 'Jacek', 'Tomek', 'Paweł']
    a = task_a(names)
    print(a)
    print()

    list_of_int = [1, 2, 3, 4, 5]
    b = task_b(list_of_int)
    print(b)
    print()

    list_of_ten_ints = [2, 2, 2, 4, 5, 6, 7, 8, 9, 10]
    c = task_c(list_of_ten_ints)
    print(c)
    print()

    d = task_d(list_of_ten_ints)
    print(d)
