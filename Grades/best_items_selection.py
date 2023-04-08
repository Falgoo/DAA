import random


def items_selection(n, m, p, v):
    if n == 0 or m == 0:
        return 0, list()

    if p[n-1] > m:
        return items_selection(n-1, m, p, v)

    else:
        v1, list1 = items_selection(n-1, m-p[n-1], p, v)
        v1 += v[n-1]
        list1.append(n)

        v2, list2 = items_selection(n-1, m, p, v)

        if v1 > v2:
            return v1, list1
        else:
            return v2, list2


random.seed(10)
n = 10
p = [random.randint(1, 10) for i in range(0, n)]
v = [random.randint(1, 10) for i in range(0, n)]
m = 20

max_val, selected_items = items_selection(n, m, p, v)
print("Max value:", max_val)
print("Selected items:", selected_items)
