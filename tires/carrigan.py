from tires.tires import Tires


class Carrigan(Tires):
    def __init__(self,sensors):
        self.sensors = sensors

    def needs_service(self):
        for number in self.sensors:
            if number >= 0.9:
                return True
        return False