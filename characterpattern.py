n=4
q = 64
for i in range(n):
    p = q + n
    for j in range(i + 1):
        print(chr(p), end=' ')
        p -= 1
    print()
# D
# D C
# D C B
# D C B A



