import sys
from typing import List, TextIO


def main() -> None:
    args: List[str] = sys.argv
    if len(args) != 2:
        print("Usage: ft_stream_management.py <file>")
        return

    filename: str = args[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    content: str = ""
    try:
        f: TextIO = open(filename, 'r')
        content = f.read()
        print("---")
        print(content, end="")
        if content and not content.endswith('\n'):
            print()
        print("---")
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {str(e)}\n")
        return

    print("Transform data:")
    print("---")

    lines: List[str] = content.split('\n')
    if lines and lines[-1] == '':
        lines.pop()

    transformed_content: str = ""
    for line in lines:
        transformed_content += line + "#\n"

    print(transformed_content, end="")
    print("---")

    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    # sys.stdin.readline() retorna str
    raw_input: str = sys.stdin.readline()
    new_file: str = raw_input.strip('\n')

    if not new_file:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_file}'")
    try:
        out_f: TextIO = open(new_file, 'w')
        out_f.write(transformed_content)
        out_f.close()
        print(f"Data saved in file '{new_file}'.")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{new_file}': {str(e)}\n")
        print("Data not saved.")


if __name__ == "__main__":
    main()
