food = []
with open("input.txt") as file:
    temp = []
    pos = 0
    for row in file:
        if row == "\n":
            sum = 0
            for i in range(pos, len(temp)):
                sum += int(temp[i])
                pos += 1
            food.append(sum)
        else:
            temp.append(row.strip())
    sum = 0
    for e in range(pos, len(temp)):
        sum += int(temp[e])
    food.append(sum)

food.sort()
sum = 0
for i in range(len(food)-1, len(food)-4, -1):
    sum += food[i]

print(sum)