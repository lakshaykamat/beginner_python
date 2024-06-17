from enum import Enum


class BodyType(Enum):
    UNDERWEIGHT = 1
    NORMAL = 2
    OVERWEIGHT = 3
    OBESE = 4

    @classmethod
    def from_bmi(cls, bmi):
        if 0 < bmi < 18.5:
            return cls.UNDERWEIGHT
        elif 18.5 <= bmi < 25:
            return cls.NORMAL
        elif 25 <= bmi < 30:
            return cls.OVERWEIGHT
        elif 30 <= bmi <= 40:
            return cls.OBESE
        else:
            raise ValueError("Invalid BMI value")


class BmiCalculator:
    def __init__(self, height_in_meter, weight_in_kg):
        if height_in_meter <= 0 or weight_in_kg <= 0:
            raise ValueError("Height and weight must be positive numbers.")
        self.__height = height_in_meter
        self.__weight = weight_in_kg
        self.__calculate_bmi()

    def __calculate_bmi(self):
        self.__bmi = round(self.__weight / (self.__height * self.__height), 2)
        self.__body_type = BodyType.from_bmi(self.__bmi)

    def info(self):
        print(f"Your BMI is {self.__bmi}")
        print(f"You are {self.__body_type.name}")

