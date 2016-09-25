HP = 0.01

def find_y():
    print('nokta koordinatlarini A = x,y seklinde giriniz')
    A1 = tuple(map(float, input('A1 = ').split(',')))
    A2 = tuple(map(float, input('A2 = ').split(',')))
    B1 = tuple(map(float, input('B1 = ').split(',')))
    B3 = tuple(map(float, input('B3 = ').split(',')))
    C1 = tuple(map(float, input('C1 = ').split(',')))
    C2 = tuple(map(float, input('C2 = ').split(',')))
    C3 = tuple(map(float, input('C3 = ').split(',')))
    D1 = tuple(map(float, input('D1 = ').split(',')))
    D2 = tuple(map(float, input('D2 = ').split(',')))
    E1 = tuple(map(float, input('E1 = ').split(',')))
    E2 = tuple(map(float, input('E2 = ').split(',')))
    F1 = tuple(map(float, input('F1 = ').split(',')))
    F2 = tuple(map(float, input('F2 = ').split(',')))

    test_area = float(input('alan degerini giriniz: '))
    y_coord = None

    def part_area(a, b, c, d = None):
        if d is None:
            area = abs(a[0] - b[0]) * abs(a[1] - c[1])
        else:
            area = abs(a[1] - c[1]) * (abs(b[0] - a[0]) + abs(c[0] - d[0])) / 2
        return area

    #PART1
    area1 = part_area(A1, A2, B1)
    print('area1 = ' + str(area1))
    new_B1 = B1
    while area1 >= test_area:
        new_B1 = (new_B1[0], new_B1[1] - 0.01)
        area1 = part_area(A1, A2, new_B1)

    y_coord = new_B1[1]

    if y_coord < B1[1]:
        print('y_coord = ' + str(y_coord))
        with open('kiris.txt', 'a') as out:
            out.write('Kiris alaninin degerinin yuksekligi ' + str(y_coord) + " cm'dir")
        return

    test_area -= area1

    #PART2
    area2 = part_area(B1, B3, C1)
    print('area2 = ' + str(area2))
    new_C1 = C1
    while area2 >= test_area:
        new_C1 = (new_C1[0], new_C1[1] - 0.01)
        area2 = part_area(B1, B3, new_C1)

    y_coord = new_C1[1]

    if y_coord < C1[1]:
        print('y_coord = ' + str(y_coord))
        with open('kiris.txt', 'a') as out:
            out.write('Kiris alaninin degerinin yuksekligi ' + str(y_coord) + " cm'dir")
        return

    test_area -= area2

    # PART3
    area3 = part_area(C2, C3, D1, D2) * 2
    print('area3 = ' + str(area3))
    new_D1 = D1
    new_D2 = D2
    while area3 >= test_area:
        new_D1 = (new_D1[0], new_D1[1] - 0.01)
        new_D2 = (new_D2[0], new_D2[1] - 0.01)
        area3 = part_area(C2, C3, new_D1, new_D2) * 2

    y_coord = new_D1[1]

    if y_coord < D1[1]:
        print('y_coord = ' + str(y_coord))
        with open('kiris.txt', 'a') as out:
            out.write('Kiris alaninin degerinin yuksekligi ' + str(y_coord) + " cm'dir")
        return

    test_area -= area3

    # PART4
    area4 = part_area(D1, D2, E1, E2) * 2
    print('area4 = ' + str(area4))
    new_E1 = E1
    new_E2 = E2
    ratio1 = abs(D1[0] - E1[0]) / abs(D1[1] - E1[1])
    ratio2 = abs(D2[0] - E2[0]) / abs(D2[1] - E2[1])
    while area4 >= test_area:
        new_E1 = (new_E1[0] - (ratio1 * 0.01), new_E1[1] - 0.01)
        new_E2 = (new_E2[0] - (ratio2 * 0.01), new_E2[1] - 0.01)
        area4 = part_area(D1, D2, new_E1, new_E2) * 2

    y_coord = new_E1[1]

    if y_coord < E1[1]:
        print('y_coord = ' + str(y_coord))
        with open('kiris.txt', 'a') as out:
            out.write('Kiris alaninin degerinin yuksekligi ' + str(y_coord) + " cm'dir")
        return

    test_area -= area4

    # PART5
    area5 = part_area(E1, E2, F1, F2) * 2
    print('area5 = ' + str(area5))
    new_F1 = F1
    new_F2 = F2
    while area5 >= test_area:
        new_F1 = (new_F1[0], new_F1[1] - 0.01)
        new_F2 = (new_F2[0], new_F2[1] - 0.01)
        area5 = part_area(E1, E2, new_F1, new_F2) * 2

    y_coord = new_F1[1] + 0.01

    if y_coord < F1[1]:
        print('y_coord = ' + str(y_coord))
        with open('kiris.txt', 'a') as out:
            out.write('Kiris alaninin degerinin yuksekligi ' + str(y_coord) + " cm'dir")
        return

    test_area -= area5



if __name__ == "__main__":
    find_y()