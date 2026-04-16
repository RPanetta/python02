#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")

    temp_str = "25"
    print(f"\nInput data is '{temp_str}'")
    result = input_temperature(temp_str)
    print(f"Temperature is now {result}°C")

    temp_str = "abc"
    print(f"\nInput data is '{temp_str}'")
    try:
        input_temperature(temp_str)
    except ValueError as err:
        print(f"Caught input_temperature error: "
              f"invalid literal for int() with base 10: {err}")
        print("\nAll tests completed - program didn't crash!")


test_temperature()
