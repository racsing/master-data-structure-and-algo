class Solution:
    def sort012(arr, n):
        count_0 = 0
        count_1 = 0
        count_2 = 0

        for i in range(n):
            if arr[i] == 0:
                count_0 += 1

            elif arr[i] == 1:
                count_1 += 1

            elif arr[i] == 2:
                count_2 += 1

        for a in range(count_0):
            arr[a] = 0
        for b in range(count_0, count_1 + count_0):
            arr[b] = 1
        for c in range(count_1 + count_0, n):
            arr[c] = 2
        return arr


N = 5
arr = [0, 2, 1, 2, 0]
print(Solution.sort012(arr, N))