lst = [3,9,4,6,2,8]

high_1 = high_2 = float('-inf')


for i in range(len(lst)):
    if lst[i] > high_1:
        high_2 = high_1
        high_1 = lst[i]
    elif lst[i] > high_2 and lst[i] != high_2:
         high_2 = lst[i]
    
print(high_1, high_2)