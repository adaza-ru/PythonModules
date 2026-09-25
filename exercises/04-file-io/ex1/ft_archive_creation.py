import sys
import typing


def main() -> None:
    args: list[str] = sys.argv

    if len(args) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    filename: str = args[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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
    except (OSError, ValueError) as e:
        print(f"Error opening file '{filename}': {str(e)}")

    if not content:
        print("No content to transform.")
        return
    else:
        print("Transform data:")
        nc: list[str] = content.splitlines()
        content = "#\n".join(nc) + "#\n"
        print("---\n")
        print(content)
        print("---")

    new_filename: str = input("Enter new file name (or empty): ")
    if new_filename:
        try:
            out_f: typing.TextIO = open(new_filename, 'w', encoding='utf-8')
            print(f"Saving data to '{new_filename}'")
            try:
                out_f.write(content)
            finally:
                out_f.close()
            print(f"Data saved in file '{new_filename}'.")
        except (OSError, ValueError) as e:
            print(f"Error creating file '{new_filename}': {str(e)}")
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
