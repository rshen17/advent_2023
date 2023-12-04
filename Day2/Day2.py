import os.path
import re


class Game():
    def __init__(self, inputstring):
        self.id = 0  # should be overwritten
        self.sets = {}
        self._parse(inputstring)
        self.valid = False
        self._validgame()
        self.minimum = 1
        self._miniumcubes()

    def _parse(self, string):
        gameid, sets = string.split(':')
        # print(gameid)
        # print(sets)
        pattern = re.compile(r'\d+')
        self.id = re.search(pattern, gameid)[0]
        # print(self.id)
        num_color = re.compile(r' (\d+) (red|green|blue)')

        self.sets = re.findall(num_color, sets)
        # print(self.sets)

    def _validgame(self):
        colorlimits = {"red": 12,
                       "green": 13,
                       "blue": 14}

        for value, color in self.sets:
            # print(value)
            if int(value) > colorlimits[color]:
                self.valid = False
                return

        self.valid = True
        return

    def _miniumcubes(self):
        colorminimums = {"red": 0,
                         "green": 0,
                         "blue": 0
                         }

        for value, color in self.sets:
            # print(value)
            if int(value) > colorminimums[color]:
                colorminimums[color] = int(value)

            # print(colorminimums.items())

        # print(colorminimums.values())
        for x in colorminimums.values():
            # print(x)
            self.minimum *= x

        # print(self.minimum)

        return


class Day2:
    def __init__(self, input_file, part):
        self.name = __name__
        self.data = input_file
        self.part = part

    def filetostringlist(self):
        with open(self.data) as f:
            return f.readlines()

    def run(self):
        print("Begining {0} test run".format(self.name))

        input_array = self.filetostringlist()
        answerA = 0
        answerB = 0
        for game in input_array:
            game.strip()  # clean string

            gameobj = Game(game)
            # print (gameobj.id)
            answerA += int(gameobj.id) if gameobj.valid else 0
            # print(gameobj.minimum)
            answerB += gameobj.minimum

        print('A: ',answerA)
        print('B: ',answerB)


if __name__ == '__main__':
    import argparse

    p = argparse.ArgumentParser(description="Test data to use")

    p.add_argument("-part", "-p", type=str, required=True)
    p.add_argument("-data", "-d", type=str, required=True)

    args = p.parse_args()

    if args.part.upper() in ['A', 'B']:
        data_file_name = "{1}{0}.txt".format(args.part.upper(), args.data)
        if os.path.exists(data_file_name):
            test = Day2(data_file_name, part=args.part.upper())
            test.run()
        else:
            raise FileNotFoundError()

    else:
        raise ValueError("Invalid command line inputs")
