import sys

a = int(input())
result = []
if a > 0:
    if a % 2 == 0:
        for i in range(1, a, 2):
            b1 = a * a - i
            b2 = a * a + i
            result.append(b1)
            result.append(b2)

    else:
        for i in range(0, a, 2):
            b1 = a * a - i
            b2 = a * a + i
            result.append(b1)
            result.append(b2)
    b = str()
    i = 0
    new_result = sorted(set(result))
    for n in new_result:
        if i < len(set(result)) - 1:
            string = str(n) + '+'
            b = b + string
            i += 1

    print(b + str(new_result[len(new_result) - 1]))

