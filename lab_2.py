def task_a(names):
    for i in range(len(names)):
        print(names[i])
    print()

def task_b(int_list):
    for i in range(len(int_list)):
        print(int_list[i]*2)
    print()

    new_list = [i*2 for i in int_list]
    print(new_list)
    print()

def task_c(list_of_ten_ints):
    for i in range(len(list_of_ten_ints)):
        if list_of_ten_ints[i] % 2 == 0:
            print(list_of_ten_ints[i])
    print()

def task_d(list_of_ten_ints):
    for i in range(len(list_of_ten_ints)):
        if i%2==0:
            print(list_of_ten_ints[i])


if __name__ == '__main__':
    names = ['Asia', 'Ania', 'Jacek', 'Tomek', 'Paweł']
    task_a(names)

    list_of_int = [1,2,3,4,5]
    task_b(list_of_int)

    list_of_ten_ints = [2,2,2,4,5,6,7,8,9,10]
    task_c(list_of_ten_ints)
    task_d(list_of_ten_ints)

