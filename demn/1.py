for n in [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]:
    sp = [x for x in range(1, n) if x % 3 == 0 or x % 5 == 0]
    print(n, sum(sp))
