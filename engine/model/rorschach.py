from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import NubbinBattery


class Rorschach():
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        self.engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        self.battery = NubbinBattery(self.current_date, self.last_service_date)
        if self.battery.needs_service() or self.engine.needs_service():
            print("service needed")
            return True
        else:
            print("service not needed")
            return False
