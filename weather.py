from random import randrange


class Weather:
    is_rain = False

    @classmethod
    def is_raining(cls):
        return cls.is_rain

    def set_raining(self):
        self.is_rain = randrange(1, 10) == 3  # rain possibility is 30%


current_weather = Weather()
