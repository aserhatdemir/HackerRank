num = int(input())
students = [[input() for j in range(2)] for n in range(num)]
[print(float(x[1])) for x in students]
print(students)