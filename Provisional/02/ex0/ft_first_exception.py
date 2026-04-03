def input_temperature(temp_str: str) -> int:
    """Converts a temperature string to an integer."""
    return int(temp_str)


def test_temperature() -> None:
    """
    Tests the input_temperature function with valid and invalid inputs,
    handling any resulting exceptions gracefully.
    """
    inputs: list[str] = ["25", "abc"]

    print("=== Garden Temperature ===\n")
    for temp_str in inputs:
        print(f"Input data is '{temp_str}'")
        try:
            temp = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C\n")
        except Exception as e:
            print(f"Caught input_temperature error: {e}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
