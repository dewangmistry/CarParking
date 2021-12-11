from ParkingLot  import ParkingLot
import sys

def main():
    parking_lot = ParkingLot()
    while True:
        user_input = input("$ ")
        parking_lot.call_function(user_input)

if __name__ == "__main__":
    main()
