sevenboom = []
for num in range(1, 100):
    if num % 7 == 0 or "7" in str(num):
        sevenboom.append("boom!")
    else:
        sevenboom.append(num)
print(sevenboom)