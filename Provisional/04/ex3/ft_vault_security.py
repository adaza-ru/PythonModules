from typing import Tuple, Union, TextIO


def secure_archive(
    filename: str, 
    action: Union[str, int] = 'r', 
    content: str = ''
) -> Tuple[bool, str]:
    """
    Función de seguridad que pasa mypy --strict.
    """
    try:
        if action == 'r' or action == 0:
            with open(filename, 'r') as f:
                data: str = f.read()
            return (True, data)

        elif action == 'w' or action == 1:
            with open(filename, 'w') as f:
                f.write(content)
            return (True, "Content successfully written to file")

        else:
            return (False, "Invalid action mode.")

    except Exception as e:
        return (False, str(e))


def test_vault() -> None:
    """Función de prueba para evitar código suelto en el top-level."""
    print("=== Cyber Archives Security ===")

    res1: Tuple[bool, str] = secure_archive('/not/existing/file', 'r')
    print(f"Using 'secure_archive' to read from a nonexistent file:\n{res1}")

    _: Tuple[bool, str] = secure_archive('ancient_fragment.txt', 'w', "[FRAGMENT 001] Digital preservation protocols\n")

    res2: Tuple[bool, str] = secure_archive('ancient_fragment.txt', 'r')
    print(f"Using 'secure_archive' to read from a regular file:\n{res2}")


if __name__ == "__main__":
    test_vault()
