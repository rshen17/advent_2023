import os.path
import re


class Day1:
    regexdict = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',

    }

    def __init__(self, input_file, part):
        self.name = __class__
        self.data = input_file
        self.part = part

    def filetostringlist(self):
        with open(self.data) as f:
            return f.readlines()

    def run(self):
        print("Begining {0} test run".format(self.name))
        # file input to list of strings
        input_array = self.filetostringlist()
        if self.part == 'A':
            pattern = re.compile(r'\d+')
        else:

            pattern = re.compile(r'(\d|one|two|three|four|five|six|seven|eight|nine)')
            reverse = r')d\|one|two|three|four|five|six|seven|eight|nine('[::-1]
            pattern2 = re.compile(reverse)

        value_list = []

        for string in input_array:
            print(string.strip())
            occurences = re.findall(pattern, string)
            if self.part == 'B':
                reverse = re.findall(pattern2, string[::-1])

            occurences = [m for m in occurences if m]
            print(occurences)
            first = occurences[0]
            if self.part == 'B':
                last = reverse[0][::-1]
            else:
                last = occurences[-1]

            # print(first)
            # print(last)
            if first in self.regexdict:
                first = self.regexdict[first]
            first = first[0]
            if last in self.regexdict:
                last = self.regexdict[last]
            last = last[-1]
            calibration_value = int(first + last)
            print(calibration_value)
            value_list.append(calibration_value)

        totalsum = sum(value_list)

        print("Answer: ", totalsum)


if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser(description="Test data to use")

    p.add_argument("-part", "-p", type=str, default='A')
    p.add_argument("-data", "-d", type=str, default='sample')

    args = p.parse_args()

    if args.part.upper() in ['A', 'B']:
        data_file_name = "{1}{0}.txt".format(args.part.upper(), args.data)
        if os.path.exists(data_file_name):
            test = Day1(data_file_name, args.part.upper())
            test.run()
        else:
            raise FileNotFoundError()

    else:
        raise ValueError("Invalid command line inputs")
