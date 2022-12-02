binary = []
with open("input.txt") as file:
    for row in file:
        binary.append(row.strip())

gamma = ""
epsilon = ""

for i in range(12):
    zeros = 0
    ones = 0
    for str in binary:
        if str[i] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

ans = int(gamma, 2) * int(epsilon, 2)

print(ans)



