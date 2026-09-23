from abc import ABC, abstractmethod


class reading(ABC):
    def __init__(self, readings):
        self.readings = list(readings)

    @abstractmethod
    def valid_reading(self, value):
        """Return whether a reading is within the valid tank range."""

    @abstractmethod
    def classify_level(self, value):
        """Return the safety category for a valid reading."""

    @abstractmethod
    def calc_average(self):
        """Return the average of all valid readings."""


class TankReading(reading):
    def valid_reading(self, value):
        return isinstance(value, (int, float)) and 0 < value < 100

    def classify_level(self, value):
        if value < 70:
            return "safe"
        if value < 90:
            return "caution"
        return "critical"

    def calc_average(self):
        valid = [value for value in self.readings if self.valid_reading(value)]
        return sum(valid) / len(valid) if valid else 0

    def summary(self):
        valid = [value for value in self.readings if self.valid_reading(value)]
        counts = {"safe": 0, "caution": 0, "critical": 0}
        for value in valid:
            counts[self.classify_level(value)] += 1
        return counts, len(self.readings) - len(valid), self.calc_average()


tank_readings = [40, 82, 95, 71, 101, -5, 65, 90]


if __name__ == "__main__":
    tank = TankReading(tank_readings)
    counts, invalid_count, average = tank.summary()

    print("safe", counts["safe"])
    print("caution", counts["caution"])
    print("critical", counts["critical"])
    print("invalid readings", invalid_count)
    print("average:", average)


