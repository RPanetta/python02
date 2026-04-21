#!/usr/bin/env python3

class GardenError(Exception):
    def __init__(self, message="Unknown garden error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Unknown water error"):
        super().__init__(message)


def test_plant_error():
    raise PlantError("The tomato plant is wilting!")


def test_water_error():
    raise WaterError("Not enough water in the tank!")


def demo_errors():
    print("\nTesting PlantError...")
    try:
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def demo_all_garden_errors():
    print("\nTesting catching all garden errors...")
    erros = [PlantError("The tomato plant is wilting!"),
             WaterError("Not enough water in the tank!"),
             ]
    for error in erros:
        try:
            raise error
        except GardenError as e:
            print(f"Caught GardenError: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===")
    demo_errors()
    demo_all_garden_errors()
    print("\nAll custom error types work correctly!")
