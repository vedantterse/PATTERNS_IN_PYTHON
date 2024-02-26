n = 5
p = 1
for i in range(n):
    for j in range(i + 1):
        print(p, end=' ')
        p += 1
    print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

n = 5
p = 1
for i in range(n):
    for j in range(i + 1):
        print(p, end=' ')
    p += 1
    print()

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5


n = 5

for i in range(n):
    p = 1
    for j in range(i, n):  # just replace range(i+1) for increasing pattern

        print(p, end=' ')
        p += 1
    print()

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1


n = 5

for i in range(1, n + 1):
    for j in range(i):
        print((i + j) % 2, end=' ')
    print()
# 1
# 0 1
# 1 0 1
# 0 1 0 1
# 1 0 1 0 1


n = 5
p = 1
for i in range(n - 1):
    for j in range(i + 1):
        print(p, end='')
    p += 1
    print()
for i in range(n):
    for j in range(i, n):
        print(p, end='')
    p -= 1
    print()

# 1
# 22
# 333
# 4444
# 55555
# 4444
# 333
# 22
# 1


n = 5
p = 1
for i in range(n - 2):

    for j in range(n - i - 1):
        print(" ", end=" ")

    for k in range(2 * i + 1):
        print(p, end=' ')
    p += 1
    print()
for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")
    for j in range(2 * i, n + 2):
        print(p, end=" ")
    p -= 1  # replace - with + for continuous pattern
    print()

#       1
#     2 2 2
#   3 3 3 3 3
# 4 4 4 4 4 4 4
#   3 3 3 3 3
#     2 2 2
#       1


n = 5
for i in range(n):
    p = 1
    for j in range(i + 1):  # replace range with (i,n) for decreasing pattern
        print(p, end='')
        p += 1
    print()

#
# 1
# 12
# 123
# 1234
# 12345


n = 5

for i in range(n):
    p = 1
    for j in range(i, n):
        print(" ", end=' ')
    for j in range(2 * (i + 1) - 1):
        print(p, end=' ')
        p += 1
    print()

#         1
#       1 2 3
#     1 2 3 4 5
#   1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8 9

# try taking out p+=1 outside for loop and p=1 outside for for a different pattern


n = 5
k = 5
for i in range(n):
    p = k
    for j in range(i):
        print(' ', end='')
    for j in range(i, n):
        print(p, end='')
        p -= 1
    k -= 1
    print()

# 54321
#  4321
#   321
#    21
#     1


n = 5
for i in range(n):
    p = 1
    for j in range(i, n):
        print(" ", end=' ')
    for j in range(i):
        print(p, end=' ')
        p += 1
    for j in range(i + 1):
        print(p, end=' ')
        p -= 1
    print()

#         1
#       1 2 1
#     1 2 3 2 1
#   1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1



n=5
for i in range(n-1):
    # Print stars on the left side
    p = 1
    for j in range(i + 1):
      print(p, end=' ')
      p += 1
    # Print spaces in the middle
    for j in range(2 * (n - i)-4):
        print(' ', end=' ')
    # Print stars on the right side
    p = i + 1
    for j in range(i + 1):
      print(p, end=' ')
      p -= 1
    print()

# 1             1
# 1 2         2 1
# 1 2 3     3 2 1
# 1 2 3 4 4 3 2 1
