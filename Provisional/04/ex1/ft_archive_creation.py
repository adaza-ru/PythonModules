import sys
from typing import IO, List


def transform_data(content: str) -> str:
    """
    Appends the 2087-compatible character '#' to each line of the content.

    Args:
        content: The raw string content to transform.

    Returns:
        The transformed string with '#' at the end of each line.
    """
    lines: List[str] = content.splitlines()
    transformed: str = "".join([f"{line}#\n" for line in lines])
    return transformed


def save_archive(filename: str, content: str) -> None:
    """
    Saves the provided content to a file, overwriting it if it exists.

    Args:
        filename: Target filename.
        content: Data to be written.
    """
    print(f"Saving data to '{filename}'")
    file_handle: IO[str]
    try:
        file_handle = open(filename, "w", encoding="utf-8")
        try:
            file_handle.write(content)
        finally:
            file_handle.close()
        print(f"Data saved in file '{filename}'.")
    except OSError as error:
        print(f"Error saving to file '{filename}': {error}")


def process_recovery(filename: str) -> str | None:
    """
    Reads the file and displays its original content.

    Returns:
        The content of the file if successful, None otherwise.
    """
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    file_handle: IO[str]
    try:
        file_handle = open(filename, "r", encoding="utf-8")
        try:
            content: str = file_handle.read()
            print("---\n" + content + "---")
            return content
        finally:
            file_handle.close()
            print(f"File '{filename}' closed.")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return None


def main() -> None:
    """Main execution flow for archive creation and transformation."""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        return

    source_file: str = sys.argv[1]
    original_content: str | None = process_recovery(source_file)

    if original_content is None:
        return

    print("Transform data:")
    new_content: str = transform_data(original_content)
    print("---\n" + new_content + "---")

    dest_file: str = input("Enter new file name (or empty): ")
    if dest_file.strip():
        save_archive(dest_file, new_content)
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
