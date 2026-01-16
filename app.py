from utils import add_numbers
from config import API_KEY
import sys

def main():
    result = add_numbers(2, 3)
    print(f"Calculation result: {result}")
    if API_KEY == "INVALID":
        raise ValueError("Invalid API_KEY")
    print("App running successfully!")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--check-config":
        if API_KEY == "INVALID":
            print("Config check failed: Invalid API_KEY")
            sys.exit(1)
        else:
            print("Config check passed")
            sys.exit(0)
    main()
