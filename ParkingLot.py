from Car import Car

class ParkingLot:
    def __init__(self) -> None:
        self.lot_capacity = 0
        self.occupied_slots = 0
        # self.nearest_slot = 1

    def call_function(self, input):
        input_vars = input.split(' ')
        try:
            if input_vars[0] == 'create_parking_lot':
                status = self.create_parking_lot(input_vars[1])
                print(f"Created a parking lot with {status} slots")
            elif input_vars[0] == "park":
                car_to_park = Car(input_vars[1], input_vars[2])
                status = self.park(car_to_park)
                if status == -1:
                    print("Sorry, parking lot is full")
                else:
                    print(f"Allocated slot number: {status}")
            elif input_vars[0] == "leave":
                if int(input_vars[1]) <= self.lot_capacity:
                    status = self.leave(int(input_vars[1]))
                    if status is True:
                        print(f"Slot number {input_vars[1]} is free")
                    else:
                        print(f"Slot is already empty")
                else:
                    print(f"Invalid slot")
        except (IndexError, ValueError):
            print(f"Invalid input")

    def create_parking_lot(self, no_of_slots):
        """
        Function to create parking lot with user provided slots
        """
        self.lot_capacity = int(no_of_slots)
        self.slots = [0] * self.lot_capacity
        return self.lot_capacity

    def get_nearest_empty_slot(self):
        """
        Function to get the nearest empty slot if any else returned -1
        """
        if self.occupied_slots < self.lot_capacity:
            empty_slot = self.slots.index(0)
        else:
            empty_slot = -1
        return empty_slot

    def park(self, car_to_park: Car) -> int:
        """
        Function to park a Car and return the slot number 
        """
        # print(self.lot_capacity)
        # print(self.slots)
        empty_slot = self.get_nearest_empty_slot()
        if empty_slot == -1:
            return -1
        else:
            self.slots[empty_slot] = car_to_park
            self.occupied_slots += 1
            return empty_slot+1

    def leave(self, slot_no: int) -> bool:
        """
        Function to remove a car from the slot and make the slot empty
        """
        # print(slot_no)
        # print(self.slots)
        if self.slots[slot_no-1] != 0:
            self.slots[slot_no-1] = 0
            self.occupied_slots -= 1
            return True
        else:
            return False

    def status(self):
        pass

    def registration_numbers_for_cars_with_colour(self, colour):
        pass
        
    def slot_numbers_for_cars_with_colour(self, colour: str):
        pass

    def slot_number_for_registration_number(self, registration_no: str):
        pass