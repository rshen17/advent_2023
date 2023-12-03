listOfLines = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        numsOnly = list(filter(lambda i: i.isdigit(), line))
        number = numsOnly[0] + numsOnly[len(numsOnly) -1 ]
        listOfLines.append(int(number))
file.close()

print(sum(listOfLines))
