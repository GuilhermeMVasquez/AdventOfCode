matches = []
with open("input.txt") as file:
    for row in file:
        matches.append(row.strip())

total = 0
for game in matches:
    count = 0
    if game[0] == "A" and game[2] == "X":
        count += 3
    elif game[0] == "B" and game[2] == "Y":
        count += 3
    elif game[0] == "C" and game[2] == "Z":
        count += 3
    elif game[0] == "A" and game[2] == "Y":
        count += 6
    elif game[0] == "B" and game[2] == "Z":
        count += 6
    elif game[0] == "C" and game[2] == "X":
        count += 6
    if game[2] == "X":
        count += 1
    elif game[2] == "Y":
        count += 2
    elif game[2] == "Z":
        count += 3
    total += count
    print(count)

print(total)