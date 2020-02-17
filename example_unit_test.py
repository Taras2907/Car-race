import unittest
from vehicles import Car, Truck, Motorcycle, Vehicle


class TddInPythonExample(unittest.TestCase):

    def test_vehicle_create_car_returns_car(self):
        race = "race"
        car = Vehicle.create_a_vehicle("Car", race)
        self.assertEqual(Car, type(car))
    
    def test_vehicle_create_car_returns_truck(self):
        race = "race"
        truck = Vehicle.create_a_vehicle("Truck", race)
        self.assertEqual(Truck, type(truck))
        
    def test_vehicle_create_car_raises_value_error_if_invalid_argument(self):
        race = "race"
        self.assertRaises(ValueError, Vehicle.create_a_vehicle, "Ferrari", race)

    def test_vehicle_create_car_raises_type_error_if_invalid_argument(self):
        race = "race"
        self.assertRaises(TypeError, Vehicle.create_a_vehicle, 11, race)


if __name__ == '__main__':
    unittest.main()