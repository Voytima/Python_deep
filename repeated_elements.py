"""
📌 Дан список повторяющихся элементов. Вернуть список с дублирующимися
элементами. В результирующем списке не должно быть дубликатов.
"""
lst = [1, 1, 2, 3, 4, 4, 5, 1, 2, 3, 4, 6, 6, 7, 8]

res = set()
for i in lst:
    if lst.count(i) >= 2:
        res.add(i)

print(list(res))
