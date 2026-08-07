def reaching_height(n, arr):
    """
    x - up - odd index
    y - down - even index
    move more - up
    move less - down

    """

    if n == 1:
        return arr

    arr.sort()
    res = [0] * n
    l, r = 0, n - 1
    ans = [-1]

    for i in range(n):
        if (i + 1) % 2 == 0:  # y - down - even index
            res[i] = arr[l]
            l += 1
        else:  # x - up - odd index

            res[i] = arr[r]
            r -= 1

    if res == arr:
        return ans

    return res

print(reaching_height(n=2, arr=[1,1]))
# arr.sort  = 2 3 4 5
# res =       5 2 4 3
