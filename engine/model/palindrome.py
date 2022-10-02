from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.nubbin import NubbinBattery


class Palindrome():
        
    def __init__(self, current_date, last_service_date, warning_light_is_on):
        self.current_date = current_date
        self.last_service_date = last_service_date
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        self.engine = SternmanEngine(self.warning_light_is_on)
        self.battery = NubbinBattery(self.current_date, self.last_service_date)
        if self.battery.needs_service() or self.engine.needs_service():
            print("Service needed")
            return True
        else:
            print("Service not required")
            return False
