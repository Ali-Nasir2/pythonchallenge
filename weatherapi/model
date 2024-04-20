
from datetime import datetime as dt
from dataclasses import dataclass


@dataclass
class Weather:
    details: dict
    date: dt
    temp: str
    descrip: str
    weather: list[dict]


    def __str__(self):
        return f'[{self.date:%H:%M}] {self.temp}C° ({self.descrip})'
