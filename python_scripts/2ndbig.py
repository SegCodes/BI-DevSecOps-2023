# With sort
""" numlist = [10, 5, 7, 8, 2, 1, 9, 1, 7]
numlist.sort()
print(numlist)
secBig = numlist[len(numlist) - 2]
print(secBig)
 """

# No sort()
numlist = [10, 5, 7, 8, 2, 1, 9, 1, 7]
print(numlist)
max = 0
max2 = 0
for num in numlist:
    if max < num:
        max2 = max
        max = num
    elif max2 < num < max:
        max2 = num
print(f"2nd biggest: {max2}")