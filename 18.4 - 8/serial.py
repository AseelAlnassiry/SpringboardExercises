"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        self.currSerial = start
        self.start = start

    def generate(self):
        res = self.currSerial
        self.currSerial += 1
        return res

    def reset(self):
        self.currSerial = self.start
    
    
