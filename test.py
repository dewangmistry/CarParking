import unittest
from unittest import result
from Car import Car
from ParkingLot import ParkingLot

class TestMyProgram(unittest.TestCase):
    parking_lot = ParkingLot()

    def test_create_parking_lot(self):
        """
        Test create_parking_lot function with 6 lots
        """
        result = self.parking_lot.create_parking_lot(6)
        self.assertEqual(6,result)

    def test_park(self):
        """
        Testing park function
        """
        car = [
            Car("KA-01-HH-1234", "White"),
            Car("KA-01-HH-9999", "White"),
            Car("KA-01-BB-0001", "Black"),
            Car("KA-01-HH-7777", "Red"),
            Car("KA-01-HH-2701", "Blue"),
            Car("KA-01-HH-3141", "Black"),
        ]

        for i in range(len(car)):
            self.assertEqual(i+1, self.parking_lot.park(car[i]))

        self.assertEqual(-1, self.parking_lot.get_nearest_empty_slot())

if __name__ == "__main__":
    unittest.main()