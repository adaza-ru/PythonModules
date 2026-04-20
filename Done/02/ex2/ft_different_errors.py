def garden_operations(operation_number: int) -> None:
    """
    Executes faulty code based on the operation_number to trigger exceptions.
    """
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        operation_number / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "a" + 1


def test_error_types() -> None:
    """Tests various operations and catches their specific exceptions."""
    print("=== Garden Error Types Demo ===")
    for i in range(5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
