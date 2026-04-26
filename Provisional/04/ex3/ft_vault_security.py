def secure_archive(
    filename: str,
    action: str | int = "r",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action in ("r", 0):
            with open(filename, "r", encoding="utf-8") as file:
                return (True, file.read())
        elif action in ("w", 1):
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        return (False, "Invalid action mode.")

    except (OSError, UnicodeDecodeError, UnicodeEncodeError) as error:
        return (False, f"Error {error.errno}: {error.strerror}")


def main() -> None:
    print("=== Cyber Archives Security ===\n")

    res1 = secure_archive("/not/existing/file", "r")
    print("Using 'secure_archive' to read from a nonexistent file: ")
    print(f"{res1}\n")

    res2 = secure_archive("etc/master.passwd", "r")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(f"{res2}\n")

    res3 = secure_archive("ancient_fragment.txt", "r")
    print("Using 'secure_archive' to read from a regular file:")
    print(f"{res3}\n")

    res4 = secure_archive("new_fragment.txt", "w", res3[1] if res3[0] else "")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(f"{res4}\n")


if __name__ == "__main__":
    main()
