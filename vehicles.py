from abc import ABCMeta, abstractmethod
from random import randrange


class Vehicle():
    __metaclass__ = ABCMeta

    def __init__(self, race):  # remove race gives argument exception
        self._distance = 0
        self._race = race
        self._vehicle_type = type(self).__name__

    @abstractmethod
    def prepare_for_lap(self):
        pass

    def move_for_an_hour(self):
        self.distance += self.speed

    @abstractmethod
    def __generate_name(self):
        pass

    @property
    def name(self):
        return self._name
  
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def vehicle_type(self):
        return self._vehicle_type
    
    @vehicle_type.setter
    def vehicle_type(self, vehicle_type):
        self._vehicle_type = vehicle_type

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, distance):
        self._distance = distance

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @staticmethod
    def create_a_vehicle(vehicle_type, race):
        if vehicle_type == "Car":
            return Car(race)
        elif vehicle_type == "Truck":
            return Truck(race)
        elif vehicle_type == "Motorcycle":
            return Motorcycle(race)


class Car(Vehicle):
    def __init__(self, race):
        super().__init__(self)
        self._name = self.__generate_name()
        self._speed = randrange(80, 110)

    def __generate_name(self):
        carNames = [
            "Presence", "Blend", "Grit",
            "Starlight", "Empyrean", "Millenium",
            "Specter", "Vigor", "Moonlight",
            "Corsair"
        ]
        first_name = carNames[randrange(len(carNames))]  #  choice random import
        second_name = carNames[randrange(len(carNames))]
        return f'{first_name} {second_name}'

    def prepare_for_lap(self, race):
        if race.has_a_broken_truck():
            self.speed = 75
        else:
            self.speed = randrange(80, 110)
        

class Motorcycle(Vehicle):
    motorcycle_number = 1

    def __init__(self, race):
        super().__init__(self)
        self._speed = 100
        self._name = self.__generate_name()
        Motorcycle.motorcycle_number += 1


    def __generate_name(self):
        return f'Motorcycle №{Motorcycle.motorcycle_number}'

    def prepare_for_lap(self, race):
        if race.is_there_raining:
            self.speed = 100 - randrange(5, 50)  # if it is raining motor travels for 5-50 km slower
        else:
            self.speed = 100


class Truck(Vehicle):
    def __init__(self, race):
        super().__init__(self)
        self._name = self.__generate_name()
        self._speed = 100
        self.__is_broken = False
        self.breakdown_turns_left = 0
    
    def __generate_name(self):
        truck_number = randrange(1, 1000)
        return f'Truck №{truck_number}'

    def prepare_for_lap(self, race):

        self.set_truck_brocken_if_chance()
        if self.is_broken and self.breakdown_turns_left == 0:
            self.speed = 0
            self.breakdown_turns_left = 2
        elif self.is_broken:
            self.breakdown_turns_left -= 1
            if self.breakdown_turns_left == 0:
                self.is_broken = False
                self.speed = 100
         
    def set_truck_brocken_if_chance(self):
        if not self.is_broken:
            self.is_broken = randrange(1, 20) == 1  # chance to become brocken is 5%

    @property
    def is_broken(self):
        return self.__is_broken

    @is_broken.setter
    def is_broken(self, true_or_false):
        self.__is_broken = true_or_false
