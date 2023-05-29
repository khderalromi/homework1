my_list = [i for i in range(2, 1001) if all(
    i % j != 0 for j in range(2, int(i ** 0.5) + 1))]

print(my_list)
