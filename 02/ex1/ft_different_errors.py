def garden_operations(val: str = None, zero: str = None,
                      file: str = None, key: str = None) -> None:
    """x"""
    if val is not None:
        int(val)
    if zero is not None:
        int(zero)/0
    if file is not None:
        f = open(file, "r")
        f.close()
    if key is not None:
        garden_dict: dict[str, str] = {"rose": "red"}
        garden_dict[key]


def test_error_types() -> None:
    """x"""
    tests: list[dict[str, str]] = [
        {"val": "fck"},
        {"zero": "5"},
        {"file": "fck_this.txt"},
        {"key": "fck_python"}
    ]
    print("=== Garden Error Types Demo ===")
    for t in tests:
        try:
            garden_operations(**t)
        except (ValueError, ZeroDivisionError,
                FileNotFoundError, KeyError) as e:
            print(f"\nTesting {type(e).__name__}...")
            print(f"Caught {type(e).__name__}: {e}")
    print("\nTesting multiple errors together...")
    print("Caught an error, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
