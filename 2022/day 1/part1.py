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

print(max(food))