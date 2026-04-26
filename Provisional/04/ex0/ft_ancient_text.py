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

    content: str = ""
    try:
        f: typing.TextIO = open(filename, 'r', encoding='utf-8')
        try:
            content = f.read()
            if content:
                if not content.endswith('\n'):
                    content += '\n'
            print("---\n")
            print(content)
            print("---")
        finally:
            f.close()
            print(f"File '{filename}' closed.")
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error opening file '{filename}': {str(e)}")


if __name__ == "__main__":
    main()
