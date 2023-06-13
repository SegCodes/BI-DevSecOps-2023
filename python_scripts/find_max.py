def list_max(my_list):
    max = my_list[0]
    for num in my_list:
        if num > max:
            max = num
    return max

def list_2max(my_list):
    max = my_list[0]
    max2 = my_list[0]
    for num in my_list:
        if max < num:
            max2 = max
            max = num
        elif max2 < num < max:
            max2 = num
    return max2

l1 = [1, 7, 5, 23, 14, 34, 12, 56, 9]
print(l1)
print(f"The max in the list: {list_max(l1)}")
print(f"The 2nd max in the list: {list_2max(l1)}")