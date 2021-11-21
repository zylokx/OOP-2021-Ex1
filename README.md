## Offline Algorithm For Elevator Scheduling

## The Algorithm

**Brief explanation:** This is a greedy algorithm. For each call, we find the elevator that takes minimum
time to arrive to the source of the call.

every elevator contains paths, each path is a list of a source and a destination that the elevator needs to
go to. at each call, we update the paths of the elevator according to the time passed since the last call
then we calculate how much time it will take every elevator to get to the source of the new call and pick the
elevator with minimum waiting time.

