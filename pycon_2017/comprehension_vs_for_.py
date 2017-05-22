import timeit

for_loop = """
test_list = []
for i in range(10000):
    test_list.append(i)
"""

comprehension = "[i for i in range(10000)]"


print(timeit.timeit(for_loop, number=10000))
print(timeit.timeit(comprehension, number=10000))
