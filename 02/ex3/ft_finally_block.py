def water_plants(plant_list: list[str]) -> None:
    try:
        for p in plant_list:
            print("Watering", p)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    good_plants: list[str] = ["tomato", "lettuce", "carrots"]
    bad_plants: list[str] = ["tomato", 3, None, "carrots"]
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")
    try:
        water_plants(good_plants)
        print("Watering completed successfully!")
    except Exception as e:
        print("Error: Cannot water", e, "- invalid plant!")
    print("Testing with error...")
    try:
        water_plants(bad_plants)
        print("Watering completed successfully!")
    except Exception as e:
        print("Error: Cannot water", e, "- invalid plant!")
    finally:
        print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
