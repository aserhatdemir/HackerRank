def main():
    num = int(input())
    # students = [[input() for j in range(2)] for n in range(num)]
    students = [[input() if (j == 0) else float(input()) for j in range(2)] for n in range(num)]
    # [float(x[1]) for x in students]

    print_second_lowest_grade(students)


def get_second_lowest_grade(lst):
    min1 = lst[0][1]
    min2 = lst[1][1]
    if min2 < min1:
        min1, min2 = min2, min1
    for i in lst[2:]:
        if i[1] < min1:
            min1, min2 = i[1], min1
        elif i[1] < min2 and i[1] != min1 or min1 == min2:
            min2 = i[1]
    return min2


def print_second_lowest_grade(lst):
    my_num = get_second_lowest_grade(lst)
    my_list = []
    for i in lst:
        if i[1] == my_num:
            my_list.append(i[0])

    my_list.sort()
    for n in my_list:
        print(n)


if __name__ == "__main__":
    main()


