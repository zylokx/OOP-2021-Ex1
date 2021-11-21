import math


class Algorithm:
    def __init__(self, building, calls):
        self.elevators = building.elevators
        self.first_elev_id = self.elevators[0].elevator_id
        self.calls = calls
        self.candidates = list()
        self.last_two_calls_timestamps_in_building = list()

    def run_algo(self):
        if len(self.calls) == 0:
            return
        first_call = True

        for call in self.calls:
            best_elevator = self.elevators[0]
            # if it's the first call, assign it to the fastest elevator
            if first_call:
                for elev in self.elevators:
                    if elev.speed > best_elevator.speed:
                        best_elevator = elev

                self.last_two_calls_timestamps_in_building.append(self.calls[0][1])
                self.last_two_calls_timestamps_in_building.append(self.calls[0][1])
                first_call = False
            else:
                best_time = math.inf
                self.last_two_calls_timestamps_in_building.append(self.last_two_calls_timestamps_in_building[1])
                self.last_two_calls_timestamps_in_building.append(self.calls[0][1])

                for elev in self.elevators:
                    # candidate_paths = elev.paths[:]
                    elev.update_elevator(self.last_two_calls_timestamps_in_building)
                    waiting_time = elev.get_waiting_time_for_future_call(call)
                    if waiting_time < best_time:
                        best_time = waiting_time
                        best_elevator = elev

            call[5] = best_elevator.elevator_id - self.first_elev_id
            best_elevator.insert_call(call, best_elevator.paths)
            best_elevator.update_direction()
