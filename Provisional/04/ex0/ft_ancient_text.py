import sys
from typing import IO


def display_fragment(filename: str) -> None:
    """
    Reads the content of a file and prints it with headers and footers.

    Args:
        filename: The path to the file to be recovered.
    """
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    file_handle: IO[str]

    try:
        file_handle = open(filename, "r", encoding="utf-8")
        try:
            content: str = file_handle.read()
            print("---")
            print(content, end="")
            print("---")
        finally:
            file_handle.close()
            print(f"File '{filename}' closed.")

    except OSError as error:
        print(f"Error opening file '{filename}': {error}")


def main() -> None:
    """Entry point of the script. Handles command line arguments."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    target_file: str = sys.argv[1]
    display_fragment(target_file)


if __name__ == "__main__":
    main()
