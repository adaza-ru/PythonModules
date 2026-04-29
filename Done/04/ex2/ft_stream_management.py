import sys
import typing


def main() -> None:
    args: list[str] = sys.argv
    content: str = ""

    if len(args) != 2:
        sys.stderr.write(f"Error: Usage: {args[0]} <file>\n")
        return

    filename: str = args[1]
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{filename}'\n")

    try:
        f: typing.TextIO = open(filename, 'r', encoding='utf-8')
        try:
            content = f.read()
            if content:
                if not content.endswith('\n'):
                    content += '\n'
            sys.stdout.write("---\n\n")
            sys.stdout.write(content)
            sys.stdout.write("\n---\n")
        finally:
            f.close()
            sys.stdout.write(f"File '{filename}' closed.\n\n")
    except (OSError, ValueError) as e:
        sys.stderr.write(f"Error: opening file '{filename}': {str(e)}\n")

    if not content:
        sys.stdout.write("No content to transform.\n")
        return
    else:
        sys.stdout.write("Transform data:\n")
        nc: list[str] = content.splitlines()
        content = "#\n".join(nc) + "#\n"
        sys.stdout.write("---\n\n")
        sys.stdout.write(content)
        sys.stdout.write("\n---\n")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()
    new_filename: str = sys.stdin.readline().strip()

    if new_filename:
        sys.stdout.write(f"Saving data to '{new_filename}'\n")
        try:
            out_f: typing.TextIO = open(new_filename, 'w', encoding='utf-8')
            try:
                out_f.write(content)
            finally:
                out_f.close()
            sys.stdout.write(f"Data saved in file '{new_filename}'.\n")
        except (OSError, ValueError) as e:
            sys.stderr.write(f"Error: creating "
                             f"file '{new_filename}': {str(e)}\n")
    else:
        sys.stdout.write("Not saving data.\n")


if __name__ == "__main__":
    main()
