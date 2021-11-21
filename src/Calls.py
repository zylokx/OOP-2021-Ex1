from enum import IntEnum
import csv


class Direction(IntEnum):
    UP = 1
    DOWN = -1


def get_direction(src, dest):
    return Direction.UP if dest > src else Direction.DOWN


class Calls:
    def __init__(self, file_name):
        self.calls = list()
        self.candidates = list()

        with open(file_name, 'r') as f:
            csv_reader = csv.reader(f, delimiter=",")
            csv_reader = [[row[0],
                           float(row[1]),
                           int(row[2]),
                           int(row[3]),
                           int(row[4]),
                           int(row[5])]
                          for row in csv_reader
                          ]

            for row in csv_reader:
                self.calls.append(row)

    def __str__(self):
        st = ""
        for row in self.calls:
            st += "call timestamp: {}, source: {}, destination: {}\n".format(row[1], row[2], row[3])

        return st

    def output_new_calls(self, file_name):
        with open(file_name, 'w') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerows(self.calls)
