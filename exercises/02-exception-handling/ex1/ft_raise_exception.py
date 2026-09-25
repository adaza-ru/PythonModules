def input_temperature(temp_str: str) -> int:
    """Converts a temperature string to an int and validates its range."""
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    """Tests the input_temperature function against various edge cases."""
    inputs = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===")
    for temp_str in inputs:
        print(f"\nInput data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
