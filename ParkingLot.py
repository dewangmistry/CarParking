from Car import Car

class ParkingLot:
    def __init__(self) -> None:
        self.lot_capacity = 0
        self.occupied_slots = 0
        # self.nearest_slot = 1

    def call_function(self, input):
        input_vars = input.split(' ')
        function_to_call = input_vars[0]
        try:
            if function_to_call == 'create_parking_lot':
                status = self.create_parking_lot(input_vars[1])
                print(f"Created a parking lot with {status} slots")
            elif function_to_call == "park":
                car_to_park = Car(input_vars[1], input_vars[2])
                status = self.park(car_to_park)
                if status == -1:
                    print("Sorry, parking lot is full")
                else:
                    print(f"Allocated slot number: {status}")
            elif function_to_call == "leave":
                if int(input_vars[1]) <= self.lot_capacity:
                    status = self.leave(int(input_vars[1]))
                    if status is True:
                        print(f"Slot number {input_vars[1]} is free")
                    else:
                        print(f"Slot is already empty")
                else:
                    print(f"Invalid slot")
            elif function_to_call == "status":
                self.status()
            elif function_to_call == "registration_numbers_for_cars_with_colour":
                result = self.registration_numbers_for_cars_with_colour(input_vars[1])
                if result == -1:
                    print("Not found")
                else:
                    print(result)
            elif function_to_call == "slot_numbers_for_cars_with_colour":
                result = self.slot_numbers_for_cars_with_colour(input_vars[1])
                if result == -1:
                    print("Not found")
                else:
                    print(result)
            elif function_to_call == "slot_number_for_registration_number":
                result = self.slot_number_for_registration_number(input_vars[1])
                if result == -1:
                    print("Not found")
                else:
                    print(result)
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
        if self.slots[slot_no-1] != 0:
            self.slots[slot_no-1] = 0
            self.occupied_slots -= 1
            return True
        else:
            return False

    def status(self):
        """
        Function to print information of all parked Car
        """
        print ("{:<8} {:<15} {:<10}".format('Slot No.','Registration No','Colour'))
        for slot_no, car in enumerate(self.slots):
            if car != 0:
                slot_no, registra, perc = slot_no+1, car.registration_no, car.colour
                print ("{:<8} {:<15} {:<10}".format( slot_no, registra, perc))

    def registration_numbers_for_cars_with_colour(self, colour: str):
        """
        Function to find registration number of a car of a colour
        """
        result = []
        for car in self.slots:
            if car != 0 and car.colour == colour:
                result.append(car.registration_no)
        if result:
            return ", ".join(result)
        else:
            return -1
        
    def slot_numbers_for_cars_with_colour(self, colour: str):
        """
        Function to find slot number of car of a colour
        """
        result = []
        for slot_no, car in enumerate(self.slots):
            if car != 0 and car.colour == colour:
                result.append(str(slot_no+1))
        if result:
            return ", ".join(result)
        else:
            return -1

    def slot_number_for_registration_number(self, registration_no: str):
        """
        Function to find slot number of in which a car with a given registration number is parked
        """
        result = -1
        for slot_no, car in enumerate(self.slots):
            if car != 0 and car.registration_no == registration_no:
                result = slot_no+1
        return result