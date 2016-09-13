lst = []
num = int(input())

for i in range(num):
    arg = input().split()
    if arg[0] == 'insert':
        lst.insert(int(arg[1]), int(arg[2]))
    elif arg[0] == 'print':
        print(lst)
    elif arg[0] == 'remove':
        lst.remove(int(arg[1]))
    elif arg[0] == 'append':
        lst.append(int(arg[1]))
    elif arg[0] == 'sort':
        lst.sort()
    elif arg[0] == 'pop':
        lst.pop()
    elif arg[0] == 'reverse':
        lst.reverse()
    else:
        print('input not supported!')
        break

