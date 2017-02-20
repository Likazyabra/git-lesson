array = [1, 2, 0, 3, 18, 14, 89, 45, 100, 0, 4]
len_arr = len(array)
i = 0
j = 0

while i < len_arr:
    j = i + 1
    while j < len_arr:
        if array[j] < array[i]:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
        j += 1
    i += 1
print(array)
