from battery.battery import Battery
import utils


class NubinBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self):
        threshold_date = utils.add_years_to_date(self.last_service_date, 4)
        return self.current_date > threshold_date
