from enum import IntEnum
import math
import Calls


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

        self.position = 0  # elevator position according to the last call timestamp
        self.calls_timestamp = list()
        self.direction = Direction.LEVEL
        self.paths = list()

    def update_direction(self):
        if len(self.paths) == 0:
            self.direction = Direction.LEVEL
        elif self.paths[0][1] > self.paths[0][0]:
            self.direction = Direction.UP
        else:
            self.direction = Direction.DOWN

    def update_elevator(self, last_two_calls_timestamps_in_building):
        if len(self.paths) == 0:
            self.direction = Direction.LEVEL
            return

        last_call_in_building_timestamp = math.ceil(last_two_calls_timestamps_in_building[1])
        penultimate_call_in_building_timestamp = math.ceil(last_two_calls_timestamps_in_building[0])

        while last_call_in_building_timestamp - penultimate_call_in_building_timestamp > 0:
            if not self.paths:
                break
            self.position = self.paths[0][0]
            current_path_dest = self.paths[0][1]

            if Calls.get_direction(self.position, current_path_dest) == Calls.Direction.UP:
                if self.position + self.speed >= current_path_dest:
                    self.paths.remove(0)
                    penultimate_call_in_building_timestamp += math.ceil(
                        self.open_time + self.close_time + self.start_time + self.stop_time
                    )
                elif self.position + self.speed < current_path_dest:
                    self.position += self.speed
                    self.paths[0][0] = self.position
            else:
                if self.position - self.speed <= current_path_dest:
                    self.paths.remove(0)
                    penultimate_call_in_building_timestamp += math.ceil(
                        self.open_time + self.close_time + self.start_time + self.stop_time
                    )
                elif self.position - self.speed > current_path_dest:
                    self.position -= self.speed
                    self.paths[0][0] = self.position

            penultimate_call_in_building_timestamp += 1

    def get_waiting_time_for_future_call(self, call):
        waiting_time = 0
        if len(self.paths) == 0:
            return abs(self.position - call[2]) / self.speed + self.start_time + self.stop_time
        candidate_paths = self.paths[:]
        self.insert_call(call, candidate_paths)
        for i in range(0, len(self.paths) - 1):
            waiting_time += abs(self.paths[i][0] - self.paths[i][1]) / self.speed
            waiting_time += self.start_time + self.stop_time + self.open_time + self.close_time

        return waiting_time

    def insert_call(self, call, paths):
        call_src = call[2]
        call_dest = call[3]

        if len(paths) == 0:
            if self.position == call_src:
                paths.append([call_src, call_dest])
            else:
                paths.append([self.position, call_src])
                paths.append([call_src, call_dest])
        else:
            last_path_dest = paths[-1][1]
            paths.append([last_path_dest, call_src])
            paths.append([call_src, call_dest])

    def __str__(self):
        st = "elevator id: {}, speed: {}, min floor: {}, max floor: {}, close time: {},"\
             "open time: {} , start time: {}, stop time: {}".format(self.elevator_id, self.speed, self.min_floor,
                                                                    self.max_floor, self.close_time,
                                                                    self.open_time, self.start_time,
                                                                    self.stop_time
                                                                    )

        st += ", paths: " + str(self.paths)

        return st
