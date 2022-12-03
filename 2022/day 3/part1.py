input = []
with open("input.txt") as file:
    for row in file:
        input.append(row.strip())

repeat = ""
for sack in input:
    aux = ""
    stop = 0
    for i in range(len(sack)//2):
        for j in range(len(sack)-1, len(sack)//2 - 1, -1):        
            if sack[i] == sack[j]:
                if sack[i] not in aux:
                    aux += sack[i]
                    break
    repeat += aux

sum = 0
for letter in repeat:
    if letter.isupper():
        sum += ord(letter) - 38
    elif letter.islower():
        sum += ord(letter) - 96

print(repeat)
print(sum)