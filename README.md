# Car race

Your task will be to simulate a race.  You will need to create 10 cars, 10
trucks, 10 motorcycles, and race them for 50 hours.  After simulating the race,
print the results.

## Program outline

Below are the required parts of a program. They are split into 3 modules
(`race`, `weather` and `vehicles`). You will run the program using `python3
race.py`.

Feel free to define more functions, methods, classes and so on, but make sure
you implement the ones below.

- `race`
  - `main()`: the entry point of our program
  - `Race`
    - `.simulate()`: simulate the race by calling `move()` on
      every vehicle 50 times; and setting whether it's raining
    - `.print_results()`: print each vehicle name, distance traveled and type
    - `.is_there_a_broken_truck`: is true if there is a broken truck on track

- `weather.current_weather`: a singleton object representing current weather
   - `.update()`: 30% chance of rain
   - `.is_raining`: is it raining currently

- `vehicles`
  - `Car`
    - if there is a broken down Truck on the track, then limit the max
      speed of cars to 75 km/h.
    - `.name`: make a list from the words here:
      http://www.fantasynamegenerators.com/car-names.php and pick 2 randomly
      for each instance.
    - `.distance`: distance traveled in the race
    - `.prepare_for_lap(race)` - set the actual speed used for the current race
    - `.move()`: travel for an hour; increases distance traveled (call this
      from `Race.simulate()` only!)

  - `Motorcycle`
    - speed is 100 km/h normally, but if it rains, travels with 5-50km/h slower
      (randomly). Doesn't care about trucks.
    - `.name`: are called "Motorcycle 1", "Motorcycle 2", "Motorcycle 3",... Unique.
    - `.distance`, `.prepare_for_lap(race)`, `.move()` - as above

  - `Truck`
    - speed is 100 km/h, but 5% chance of breaking down for 2 turns
    - `.name`: truck drivers are boring. They call all their trucks a random
      number between 0 and 1000.
    - `.breakdown_turns_left`: how long it's still broken down
    - `.distance`, `.prepare_for_lap(race)`, `.move()` - as above

## Hints

* Car, Motocycle and Truck have some common behavior, you should probably
  create a common superclass for them.
* The fields (such as `distance`, `name` or `speed`) can be either regular
  fields, or properties (using
  [`@property`](https://docs.python.org/3/library/functions.html#property)). Use
  properties if it's more convenient to compute a value on the fly.
* Note that `is_raining` and `is_there_a_broken_truck` should also be either
  fields or properties (not regular methods).
* You might need [static methods](https://docs.python.org/3/library/functions.html#staticmethod)
  and static variables (see [class objects](https://docs.python.org/3/tutorial/classes.html#class-objects) in
  Python docs).
