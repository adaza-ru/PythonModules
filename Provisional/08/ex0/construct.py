import sys
import os
import site


def matrix():
    is_venv: bool = sys.prefix != sys.base_prefix
    print(f"DEBUG: sys.prefix = {sys.prefix}")
    print(f"DEBUG: sys.base_prefix = {sys.base_prefix}\n")

    if not is_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")
        print("\nThen run this program again.")
    else:
        print(f"DEBUG: Virtual Environment Name:"
              f" {os.path.basename(sys.prefix)}")
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")

        print("\nPackage installation path:")
        packages_path: str = site.getsitepackages()[0]
        print(packages_path)


if __name__ == "__main__":
    matrix()
