""" Half Diamond star pattern
    *
    **
    ***
    ****
    *****
    ******
    *****
    ****
    ***
    **
    *
"""

def halfDiamondStar(N):
    for i in range(N+1):
        for j in range(i):
            print(' * ', end='')
        print("\n")
        
    for i in range(N-1, 0, -1):
        for j in range(i):
            print(' * ', end='')
        print("\n")


# Input
halfDiamondStar(4)

    