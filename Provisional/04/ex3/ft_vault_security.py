def secure_archive(
    filename: str,
    action: str | int = "r",
    content: str = "",
) -> tuple[bool, str]:
    try:
        if action == "r" or action == 0:
            with open(filename, "r") as file:
                return (True, file.read())
        if action == "w" or action == 1:
            with open(filename, "w") as file:
                file.write(content)
            return (True, "Content successfully written to file")
        return (False, "Invalid action mode.")
    except OSError as error:
        return (False, str(error))


def main() -> None:
    print("=== Cyber Archives Security ===")

    res1 = secure_archive("/not/existing/file", "r")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(res1)

    res2 = secure_archive("/etc/master.passwd", "r")
    print("Using 'secure_archive' to read from an inaccessible file:")
    print(res2)

    res3 = secure_archive("ancient_fragment.txt", "r")
    print("Using 'secure_archive' to read from a regular file:")
    print(res3)

    res4 = secure_archive("new_fragment.txt", "w", res3[1] if res3[0] else "")
    print("Using 'secure_archive' to write previous content to a new file:")
    print(res4)


if __name__ == "__main__":
    main()
