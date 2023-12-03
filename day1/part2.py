listOfLines = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        numericWords = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        word = ""
        for char in line:
            if char.isdigit():
                break
            word = word + char
            for i in range(len(numericWords)):
                if numericWords[i] in word:
                    line = line.replace(numericWords[i], str(i), 1)
                    break
        word = ""
        for char in reversed(line):
            if char.isdigit():
                break
            word = char + word
            for i in range(len(numericWords)):
                if numericWords[i] in word:
                    line = line.replace(numericWords[i], str(i))
                    break
        numsOnly = list(filter(lambda i: i.isdigit(), line))
        number = numsOnly[0] + numsOnly[len(numsOnly) -1 ]
        listOfLines.append(int(number))
file.close()

print(sum(listOfLines))
