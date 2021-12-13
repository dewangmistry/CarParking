from ParkingLot  import ParkingLot
import argparse
import sys

def main():
    parking_lot = ParkingLot()
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=False, dest='input_file')
    args = parser.parse_args()
    
    if args.input_file:
        with open(args.input_file) as file:
            for inputs in file:
                user_input = inputs.rstrip('\n')
                parking_lot.call_function(user_input)
    else:
        while True:
            user_input = input("$ ")
            parking_lot.call_function(user_input)
	
if __name__ == "__main__":
    main()
