def nthUglyNumber(n):
    base = [2, 3, 4, 5]

    while len(base) < n+10:
        for i in range(len(base)):
            if (base[i] * 2) not in base:
                base.append(base[i] * 2)
            if (base[i] * 3) not in base:
                base.append(base[i] * 3)
            if (base[i] * 5) not in base:
                base.append(base[i] * 5)

    base.append(1)
    base = sorted(base)

    print(base)
    return base[n - 1]

print(nthUglyNumber(12))
k = [1,3,2]
k.sort()
print(k)