from Car import Car

class ParkingLot:
    def __init__(self) -> None:
        self.lot_capacity = 0
        self.occupied_slots = 0

    def call_function(self, input):
        input_vars = input.split(' ')
        try:
            if input_vars[0] == 'create_parking_lot':
                status = self.create_parking_lot(input_vars[1])
                print(f"Created a parking lot with {status} slots")
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
        pass

    def park(self, registration_no: str, colour: str) -> int:
        pass

    def leave(self, slot_no: int) -> bool:
        pass

    def status(self):
        pass

    def registration_numbers_for_cars_with_colour(self, colour):
        pass
        
    def slot_numbers_for_cars_with_colour(self, colour: str):
        pass

    def slot_number_for_registration_number(self, registration_no: str):
        pass