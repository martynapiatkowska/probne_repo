print('hej, tu nowe repo')


def merged(list1, list2):
    list1.extend(list2)
    for element in list1[:]:
        if list1.count(element) >= 2:
            list1.remove(element)
    return list1

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

print(merged(list1, list2))


def factorial(keyin):
    if keyin == 1 or keyin == 0:
        return 1
    elif keyin < 0:
        return 'no tak to ziomek nie działa'
    else:
        return keyin * factorial(keyin - 1)

print(factorial(int(input('jaką liczbę kurwa ten? '))))
