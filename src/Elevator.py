from enum import IntEnum


class Direction(IntEnum):
    LEVEL = 0  # When the elevator is idle the doors are open
    UP = 1
    DOWN = -1


class Elevator:
    def __init__(self, elevator_id, speed, min_floor, max_floor, close_time, open_time, start_time, stop_time):
        self.elevator_id = elevator_id
        self.speed = speed  # Floors per second
        self.min_floor = min(min_floor, max_floor)
        self.max_floor = max(min_floor, max_floor)
        self.close_time = close_time
        self.open_time = open_time
        self.start_time = start_time
        self.stop_time = stop_time

        self.position = 0
        self.direction = Direction.LEVEL
        self.paths = list()

    def __str__(self):
        st = "elevator id: {}, speed: {}, min floor: {}, max floor: {}, close time: {}, open time: {}" \
             ", start time: {}, stop time: {}, " \
             "current position: {}".format(self.elevator_id, self.speed, self.min_floor, self.max_floor,
                                           self.close_time, self.open_time, self.start_time,
                                           self.stop_time, self.position
                                           )

        st += ", paths: " + str(self.paths)

        return st
