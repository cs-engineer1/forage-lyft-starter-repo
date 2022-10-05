from serviceable import Serviceable


class Car(Serviceable):

    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        if self.battery.needs_service() or self.engine.needs_service() or self.tires.needs_service():
            print("Service Needed")
            return True
        else:
            print("Service not required")
            return False

