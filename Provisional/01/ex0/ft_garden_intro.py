#!/usr/bin/env python3
"""
Exercise 0: Plant introductory script.
This script demonstrates the basic structure of a Python program.
"""

def main() -> None:
    """Main function to display basic plant information."""
    name: str = "Rose"
    height: int = 25
    age: int = 30

    print("Welcome to My Garden")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("End of Program")

if __name__ == "__main__":
    main()