t = ()
num = int(input())

#e_list = input().split()
#if len(e_list) == num:
#    e_list = map(int, e_list)
#    t = tuple(e_list)
#else:
#    print('wrong input')

t = tuple(map(int, input().split()))
if len(t) == num:
    print(hash(t))
else:
    print('wrong input')
