N = int(input())
n_list = [int(n) for n in input().split()]
sec_flag = False
max_flag = False

for i in n_list:
    if not max_flag:
        n_max = i
        max_flag = True
    elif not sec_flag:
        if i > n_max:
            n_sec = n_max
            n_max = i
            sec_flag = True
        elif i is n_max:
            pass
        else:
            n_sec = i
            sec_flag = True
    elif i > n_max:
        n_sec = n_max
        n_max = i
    elif i is n_max:
        pass
    elif i > n_sec:
        n_sec = i
    else:
        pass

print(n_sec)
