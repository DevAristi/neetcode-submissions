import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, length, width=None):
        if width is None:
            radius = length
            area = math.pi * (radius ** 2)
            return round(area, 2)
        return length * width

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
