lst = [1, 11, 2, 3, 8, 9, 14, 89, 45]

len_lst = len(lst) - 1
j = len_lst

while j >= 0:
    if j < len_lst/2:
        break

    lst[len_lst - j], lst[j] = lst[j], lst[len_lst - j]
    j -= 1

print(lst)

# Это я погорячилась :)
"""lst = [11, 2, 3, 8, 14, 89, 45]
len_lst = len(lst) - 1
j = len_lst

while j >= 0:
    if type(lst[j]) == str:
        n = len(str(int(float(lst[j]))) + '.')
        n = lst[j][n]
    else:
        n = lst[j]
        
    lst[len_lst-j] = str(n) + '.' + str(lst[len_lst - j])
    j -=1

i = 0
while i <= len_lst:
    lst[i] = int(float(lst[i]))
    i += 1
    
print(lst)"""