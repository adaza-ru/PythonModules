from typing import Tuple


def secure_archive(
    filename: str,
    mode: str = "r",
    content: str = ""
) -> Tuple[bool, str]:
    """
    Provides safe access to files for reading or writing.

    Args:
        filename: The path to the file.
        mode: The operation mode ('r' for read, 'w' for write).
        content: The data to write if mode is 'w'.

    Returns:
        A tuple (Success, Data/Error Message).
    """
    try:
        with open(filename, mode, encoding="utf-8") as file_handle:
            if mode == "w":
                file_handle.write(content)
                return True, "Content successfully written to file"

            data: str = file_handle.read()
            return True, data

    except OSError as error:
        return False, str(error)


def main() -> None:
    """Demonstrates the security protocols of the vault."""
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    secure_archive("vault_test.txt", "w", "Data security protocol 2087")

    print("\nUsing 'secure_archive' to read from a regular file:")
    result = secure_archive("vault_test.txt", "r")
    print(result)

    if result[0]:
        print("\nUsing 'secure_archive' to"
              " write previous content to a new file:")
        print(secure_archive("backup_vault.txt", "w", result[1]))


if __name__ == "__main__":
    main()
