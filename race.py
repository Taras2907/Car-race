from vehicles import Car, Motorcycle, Truck
from weather import current_weather


class Race:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def simulate(self):
        # TODO
        pass

    def print_results(self):
        # TODO
        pass


def create_vehicles(race):
    # TODO
    pass


def main():
    race = Race()
    create_vehicles(race)

    race.simulate()
    race.print_results()


if __name__ == '__main__':
    main()
