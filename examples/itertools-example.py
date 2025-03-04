import itertools

perm = itertools.permutations([1, 2, 3, 4])
print(perm)

for element in perm:
    print(element)

for element in itertools.repeat(5):
    print(element)
