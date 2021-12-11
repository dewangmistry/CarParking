import unittest
from ParkingLot import ParkingLot

class TestMyProgram(unittest.TestCase):
    def test_create_parking_lot(self):
        """
        Test create_parking_lot function with 6 lots
        """
        parking_lot = ParkingLot()
        result_1 = parking_lot.create_parking_lot(6)
        self.assertEqual(6,result_1)

if __name__ == "__main__":
    unittest.main()