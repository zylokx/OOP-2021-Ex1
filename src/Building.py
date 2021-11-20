import json
from Elevator import Elevator
import collections


class Building:
    def __init__(self, file_name):
        try:
            with open(file_name, 'r') as f:
                data = json.load(f)
                self.min_floor = data["_minFloor"]
                self.max_floor = data["_maxFloor"]
                self.elevators = []
                for elev in data["_elevators"]:
                    self.elevators.append(Elevator(elev["_id"], elev["_speed"], elev["_minFloor"],
                                                   elev["_maxFloor"], elev["_closeTime"], elev["_openTime"],
                                                   elev["_startTime"], elev["_stopTime"]
                                                   )
                                          )
        except IOError as e:
            print(e)

    def __str__(self):
        st = "Building:\n---------\nmin_floor = {}\nmax_floor = {}\n".format(self.min_floor, self.max_floor)
        st += "elevators:"
        for elev in self.elevators:
            st += "\n" + elev.__str__()

        return st
