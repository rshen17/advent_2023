listOfLines = []

with open('input.txt') as file:
    lines = file.readlines()
    for line in lines:
        numericWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        numerics = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }
        for i in range(len(numericWords)):
            line = line.replace(i[num], )
        line.replace()
        numsOnly = list(filter(lambda i: i.isdigit(), line))
        number = numsOnly[0] + numsOnly[len(numsOnly) -1 ]
        listOfLines.append(int(number))
file.close()

print(sum(listOfLines))
