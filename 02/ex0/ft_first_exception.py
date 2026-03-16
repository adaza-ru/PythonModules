def check_temperature(temp_str: str) -> None:
    """x"""
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp: int = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Temperature {temp}°C is perfect for plants!")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    """x"""
    print("=== Garden Temperature Checker ===")
    temps: list[str] = ["25", "abc", "100", "-50"]
    for t in temps:
        check_temperature(t)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
