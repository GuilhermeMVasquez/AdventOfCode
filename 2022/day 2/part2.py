matches = []
with open("input.txt") as file:
    for row in file:
        matches.append(row.strip())
# X = lose
# Y = draw
# Z = win
# A = rock = 1
# B = paper = 2
# C = scissors = 3

total = 0
for game in matches:
    count = 0
    if game[2] == "X":
        if game[0] == "A":
            count += 3
        elif game[0] == "B":
            count += 1
        elif game[0] == "C":
            count += 2
    elif game[2] == "Y":
        count += 3
        if game[0] == "A":
            count += 1
        elif game[0] == "B":
            count += 2
        elif game[0] == "C":
            count += 3
    elif game[2] == "Z":
        count += 6
        if game[0] == "A":
            count += 2
        elif game[0] == "B":
            count += 3
        elif game[0] == "C":
            count += 1
    total += count

print(total)