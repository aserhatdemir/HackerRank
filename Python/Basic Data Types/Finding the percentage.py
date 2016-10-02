def main():
   num = int(input())
   s_dict = {}
   for i in range(num):
       name, g1, g2, g3 = input().split()
       s_dict[name] = [float(g1), float(g2), float(g3)]
   s_key = input()

   if s_key in s_dict:
       print(get_percentage(s_dict[s_key]))


def get_percentage(lst):
    s = 0
    for i in lst:
        s += i
    p = s / len(lst)
    return format(p, '.2f')


if __name__ == "__main__":
    main()


