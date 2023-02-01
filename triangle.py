a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

if (a + b) < c:
    res = "Треугольника с такими сторонами не существует"
elif (a + c) < b:
    res = "Треугольника с такими сторонами не существует"
elif (b + c) < a:
    res = "Треугольника с такими сторонами не существует"
elif a == b == c:
    res = "Треугольник равносторонний"
elif a != b and b != c and a != c:
    res = "Треугольник разносторонний"
else:
    res = "Треугольник равнобедренным"

print(res)

# Option 2 (shorter):
# if (a + b) < c or (a + c) < b or (b + c) < a:
#     res = "Треугольника с такими сторонами не существует"
# elif a == b == c:
#     res = "Треугольник равносторонний"
# elif a != b and b != c and a != c:
#     res = "Треугольник разносторонний"
# else:
#     res = "Треугольник равнобедренным"
#
# print(res)
