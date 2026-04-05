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


def log_error(message: str) -> None:
    """
    Writes an error message to the standard error stream (stderr).

    Args:
        message: The error description to be logged.
    """
    sys.stderr.write(f"[STDERR] {message}\n")
    sys.stderr.flush()


def get_user_input(prompt: str) -> str:
    """
    Gets user input from stdin without using the input() built-in.

    Args:
        prompt: The message to display before waiting for input.

    Returns:
        The string entered by the user, stripped of the trailing newline.
    """
    sys.stdout.write(prompt)
    sys.stdout.flush()
    line: str = sys.stdin.readline()
    return line.rstrip("\n")


def save_archive(filename: str, content: str) -> bool:
    """
    Saves the provided content to a file.

    Args:
        filename: Target filename.
        content: Data to be written.

    Returns:
        True if the save was successful, False otherwise.
    """
    sys.stdout.write(f"Saving data to '{filename}'\n")
    file_handle: IO[str]
    try:
        file_handle = open(filename, "w", encoding="utf-8")
        try:
            file_handle.write(content)
        finally:
            file_handle.close()
        sys.stdout.write(f"Data saved in file '{filename}'.\n")
        return True
    except OSError as error:
        log_error(f"Error opening file '{filename}': {error}")
        return False


def process_recovery(filename: str) -> str | None:
    """
    Reads the file and displays its original content using stdout.

    Returns:
        The content of the file if successful, None otherwise.
    """
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")

    file_handle: IO[str]
    try:
        file_handle = open(filename, "r", encoding="utf-8")
        try:
            content: str = file_handle.read()
            sys.stdout.write("---\n" + content + "---\n")
            return content
        finally:
            file_handle.close()
            sys.stdout.write(f"File '{filename}' closed.\n")
    except OSError as error:
        log_error(f"Error opening file '{filename}': {error}")
        return None


def main() -> None:
    """Main logic for stream management and data preservation."""
    if len(sys.argv) != 2:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>\n")
        return

    source_file: str = sys.argv[1]
    original_content: str | None = process_recovery(source_file)

    if original_content is None:
        return

    sys.stdout.write("Transform data:\n")
    new_content: str = transform_data(original_content)
    sys.stdout.write("---\n" + new_content + "---\n")

    dest_file: str = get_user_input("Enter new file name (or empty): ")
    if dest_file:
        success: bool = save_archive(dest_file, new_content)
        if not success:
            sys.stdout.write("Data not saved.\n")
    else:
        sys.stdout.write("Not saving data.\n")


if __name__ == "__main__":
    main()
