def task_1(name: str, surname: str) -> str:
    result = 'Cześć {} {}'.format(name, surname)
    return result


def task_2(numb1: int, numb2: int) -> int:
    return numb1 * numb2


def task_3(numb: int) -> bool:
    if (numb % 2):
        return True
    else:
        return False


def task_4(numb1: int, numb2: int, numb3: int) -> bool:
    return numb1 + numb2 >= numb3


def task_5(list_1: list, numb: int) -> bool:
    result = False
    for i in list_1:
        if i == numb:
            result = True
            continue
    return result


def task_6(list_1: list, list_2: list) -> list:
    return list(i ** 3 for i in (list(set(list_1 + list_2))))


if __name__ == '__main__':
    print(task_1("Joanna", "Krawczyk"))

    print(task_2(1, 2))

    condition = task_3(56)
    if (condition):
        print("Liczba nieparzysta")
    else:
        print("Liczba parzysta")

    print(task_4(1, 1, 3))

    list_of_numbs = [5, 7, 1]
    print(task_5(list_of_numbs, 7))

    print(task_6([1, 1, 1, 1], [1, 1, 1, 8]))
