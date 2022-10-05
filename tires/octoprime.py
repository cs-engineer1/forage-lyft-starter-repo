from tires.tires import Tires


class Octoprime(Tires):
    def __init__(self,sensors):
        self.sensors = sensors

    def needs_service(self):
        sum = 0
        for number in self.sensors:
            sum += number
        if sum >= 3:
            return True
        else:
            return False