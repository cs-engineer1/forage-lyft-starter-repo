from abc import ABC

from battery.battery import Battery


class NubbinBattery(Battery, ABC):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self):
        self.service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        return self.service_threshold_date < self.current_date