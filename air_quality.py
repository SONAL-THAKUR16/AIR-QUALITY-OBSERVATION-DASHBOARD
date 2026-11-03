class StationReading:
    def __init__(self, date, station, pm25, temperature):
        self.date = date
        self.station = station
        self.pm25 = pm25
        self.temperature = temperature

    def is_valid(self):
        return self.pm25 >= 0 and self.temperature >= -50

    def is_anomaly(self):
        return self.pm25 > 60