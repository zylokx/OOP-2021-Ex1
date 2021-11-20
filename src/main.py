import argparse
from Building import Building
from Elevator import Elevator

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ex1: offline elevator algorithm')
    parser.add_argument('building', help='json file name that contains the building')
    parser.add_argument('calls', help='csv file name that contains the calls')
    parser.add_argument('output', help='name of the output csv file')
    args = parser.parse_args()

    building = Building(args.building)
    print(building)