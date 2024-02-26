n=5
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print()


# *
# **
# ***
# ****
# *****

n=5
for i in range(n):
    for j in range(i,n):
        print("*",end='')
    print()

# *****
# ****
# ***
# **
# *

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end='')
    for j in range(i+1):
        print("*",end='')
    print()


 #     *
 #    **
 #   ***
 #  ****
 # *****

n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n):
        print("*",end='')
    print()

 # *****
 #  ****
 #   ***
 #    **
 #     *




n = 5  # 3
for i in range(n):
    for j in range(i,n):
        print(" ",end='')
    for j in range(2*(i+1)-1):
        print("*",end='')
    print()
#alternative

for i in range(n):

    for j in range(i, n):
        print(" ", end=' ')
    for j in range(i):
        print("*", end=' ')

    for j in range(i + 1):
        print('*', end=' ')

    print()
 #
 #     *
 #    ***
 #   *****
 #  *******
 # *********

n = 5  # 3
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(2 * (n - i) - 1):
        print("*",end='')
    print()

 # *********
 #  *******
 #   *****
 #    ***
 #     *




# SPACES
# FOR TRAINGULAR SPACES DOWNWARD
# range(2*(n-i)-2):  note: -2 is adjustable
# print(" ",end="")

## FOR TRAINGULAR SPACES UPWARD
# range(2*i (+-)): note: -+ is adjustable
# print(" ",end="")

# ------------------------------------------------------------------------------- #
def nStarTriangle(n: int) -> None:
    for i in range(n-1):
        # Print stars on the left side
        for j in range(i + 1):
            print('*', end=' ')
        # Print spaces in the middle
        for j in range(2 * (n - i) - 2):
            print(' ', end=' ')
        # Print stars on the right side
        for j in range(i + 1):
            print('*', end=' ')
        print()
    for i in range(n):
        for j in range(i,n):
            print('*', end=' ')
        for j in range(2 * i ):
            print(' ', end=' ')

            # Print stars on the right side
        for j in range(i,n):
            print('*', end=' ')

        print()


nStarTriangle(5)



# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *

def nStarTriangle(n: int) -> None:

    for i in range(n):
        for j in range(i,n):
            print('*', end=' ')
        for j in range(2 * i ):
            print(' ', end=' ')

            # Print stars on the right side
        for j in range(i,n):
            print('*', end=' ')

        print()
    for i in range(n):
        # Print stars on the left side
        for j in range(i + 1):
            print('*', end=' ')
        # Print spaces in the middle
        for j in range(2 * (n - i) - 2):
            print(' ', end=' ')
        # Print stars on the right side
        for j in range(i + 1):
            print('*', end=' ')
        print()
n = 5
nStarTriangle(n)

# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
# *                 *
# * *             * *
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *


n=5
for i in range(n-2):

    for j in range(n - i - 1):
        print(" ", end=" ")

    for k in range(2 * i + 1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(2*i,n+2):
        print("*", end=" ")
    print()

  #       *
  #     * * *
  #   * * * * *
  # * * * * * * *
  #   * * * * *
  #     * * *
  #       *


n=5
for i in range(n - 1):
    for j in range(i + 1):
        print('*', end='')
    print()
for i in range(n):
    for j in range(i, n):
        print('*', end='')
    print()

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()

# *****
# *   *
# *   *
# *   *
# *****