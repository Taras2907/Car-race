from weather import current_weather
from vehicles import Vehicle


class Race:

    def __init__(self):
        self.vehicles = []
        self.trucks = []
        self.is_a_brocken_truck = False

    def add_vehicle(self, vehicle):
        if vehicle.vehicle_type == "Truck":
            self.trucks.append(vehicle)
        self.vehicles.append(vehicle)

    def simulate(self):
        laps = 50
        for lap in range(laps):
            self.prepare_vehicles_for_lap()
            for vehicle in self.vehicles:
                vehicle.move_for_an_hour()

    def prepare_vehicles_for_lap(self):
        current_weather.set_raining()
        for vehicle in self.vehicles:
            vehicle.prepare_for_lap(self)
            
    def print_results(self):
        for vehicle in self.vehicles:
            print(f'Vehicle name: {vehicle.name}, distance travelled is {vehicle.distance}')

    def has_a_broken_truck(self):
        for truck in self.trucks:
            if truck.is_brocken:
                return True
        return False

    def is_there_raining():
        return current_weather.is_raining


def create_vehicles(race):
    add_ten_vehicles("Car", race)
    add_ten_vehicles("Truck", race)
    add_ten_vehicles("Motorcycle", race)


def add_ten_vehicles(vehicle_type, race):
    for n in range(0, 10):
        new_vehicle = Vehicle.create_a_vehicle(vehicle_type, race)
        race.add_vehicle(new_vehicle)


def main():
    race = Race()
    create_vehicles(race)
    race.simulate()
    race.print_results()


if __name__ == '__main__':
    main()
