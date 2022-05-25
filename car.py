from abc import ABC


class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        print(str(self.engine.needs_service()) + " " + str(self.battery.needs_service()))
        return self.engine.needs_service() or self.battery.needs_service()
