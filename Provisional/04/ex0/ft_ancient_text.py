import sys
import typing


def main() -> None:
    args: list[str] = sys.argv

    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = args[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f: typing.TextIO = open(filename, 'r')
        content: str = f.read()
        print("---")
        print(content, end="")
        if content and not content.endswith('\n'):
            print()
        print("---")
        f.close()
        print(f"File '{filename}' closed.")
    except OSError as e:
        print(f"Error opening file '{filename}': {str(e)}")


if __name__ == "__main__":
    main()
