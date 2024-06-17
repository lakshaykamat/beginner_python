from BmiCalculator import BmiCalculator

height = float(input("Enter Height in Meter: "))
weight = int(input("Enter Weight in Kilogram: "))

bmiCalculator = BmiCalculator(height, weight)
bmiCalculator.info()
