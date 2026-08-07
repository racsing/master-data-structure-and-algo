# TC: O(n)
# SC: O(1)

def encode(arr):
    Str = ''
    current = arr[0]
    count = 0
    for char in arr:
        if current != char:
            Str += current + str(count)
            count = 0
            current = char
        count += 1
    Str += current + str(count)

    return Str


print(encode('aaabbbcccc'))
