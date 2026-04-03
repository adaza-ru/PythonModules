import sys


def main() -> None:
    """
    Main function to parse and display command-line arguments.
    It identifies the program name and lists any additional parameters.
    """
    print("=== Command Quest ===")

    program_name: str = sys.argv[0]
    args_received: list[str] = sys.argv[1:]
    num_args: int = len(args_received)

    print(f"Program name: {program_name}")

    if num_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {num_args}")
        for index in range(num_args):
            print(f"Argument {index + 1}: {args_received[index]}")

    print(f"Total arguments: {len(sys.argv)}\n")


if __name__ == "__main__":
    main()
