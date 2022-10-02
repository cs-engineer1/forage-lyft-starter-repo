from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarFactory:
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Calliope(current_date, last_service_date, current_mileage, last_service_mileage)
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Glissade(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_palindrome(self, current_date, last_service_date, warning_light_is_on):
        return Palindrome(current_date, last_service_date, warning_light_is_on)

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Rorschach(current_date, last_service_date, current_mileage, last_service_mileage)

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Thovex(current_date, last_service_date, current_mileage, last_service_mileage)
