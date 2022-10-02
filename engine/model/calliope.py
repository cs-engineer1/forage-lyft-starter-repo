from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.spindler import SpindlerBattery

class Calliope():
    def __init__(self, current_date, last_service_date, current_mileage, last_service_mileage):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        self.engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        self.battery = SpindlerBattery(self.current_date, self.last_service_date)
        if self.battery.needs_service() or self.engine.needs_service():
            print("Service Needed")
            return True
        else:
            print("Service not required")
            return False

