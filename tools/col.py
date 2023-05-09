def my_zip(it1, it2):
    return zip(it1, it2)


it1 = [1, 2, 3]
it2 = ['a', 'b', 'c']
for x, y in zip(it1, it2):
    print(x, y)


