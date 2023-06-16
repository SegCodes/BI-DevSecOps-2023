alicestr = open("alice.txt", "r", encoding="UTF-8").read()
alicemod = ""

for char in alicestr:
    if(char.isupper()):
        alicemod += char.lower()
    elif(char.islower()):
        alicemod += char
    else:
        alicemod += " "

print(alicemod)