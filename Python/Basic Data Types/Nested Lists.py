def print_second_grade(lst):
    sec_flag = False
    max_flag = False

    for i in lst:
        if not max_flag:
            n_max = i[1]
            max_flag = True
        elif not sec_flag:
            if i[1] > n_max:
                n_sec = n_max
                n_max = i[1]
                sec_flag = True
            elif i[1] is n_max:
                pass
            else:
                n_sec = i[1]
                sec_flag = True
                print(i[0])
        elif i[1] > n_max:
            n_sec = n_max
            n_max = i[1]
        elif i[1] is n_max:
            pass
        elif i[1] > n_sec:
            n_sec = i[1]
            print(i[0])
        else:
            pass



num = int(input())
#students = [[input() for j in range(2)] for n in range(num)]
students = [[input() if (j == 0) else float(input()) for j in range(2)] for n in range(num)]
#[float(x[1]) for x in students]

print_second_grade(students)

print(students)


