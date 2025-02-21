""" Simple Diamond star pattern

For size = 8      (sp, *)

  * * * * * *      2,  6
* * * * * * * *    0,  8
  * * * * * *      2,  6
    * * * *        4,  4
      * *          6,  2

"""

def simpleDiamond(N):

    spaces = N

    for i in range(N//2 + 2):
        for j in range(N):
            if j < i-1:
                print(' ', end=" ")
            elif j > spaces:
                print(' ', end=" ")
            elif (i == 0 and j == 0) | (i == 0 and j == N-1):
                print(' ', end=" ")
            else:
                print('*', end=" ")
                
        spaces -= 1
        print()


# Input
simpleDiamond(8)

    