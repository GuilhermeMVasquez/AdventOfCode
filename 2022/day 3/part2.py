input = []
with open("input.txt") as file:
    for row in file:
        input.append(row.strip())

repeat = ""
for i in range(0, len(input), 3):
    aux = ""
    stop = 0
    for j in range(len(input[i])):
        for h in range(len(input[i+1])):    
            if input[i][j] == input[i+1][h]:
                for k in range(len(input[i+2])):
                    if input[i][j] == input[i+2][k]:
                        if input[i][j] not in aux:
                            aux += input[i][j]
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