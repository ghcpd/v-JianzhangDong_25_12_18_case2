from utils import add_numbers
from config import API_KEY

def main():
    result = add_numbers(2, 3)
    print(f"Calculation result: {result}")
    if API_KEY == "INVALID":
        raise ValueError("Invalid API_KEY")
    print("App running successfully!")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-config", action="store_true", help="Validate configuration and exit")
    args = parser.parse_args()
    if args.check_config:
        if API_KEY == "INVALID":
            print("Configuration invalid: API_KEY is set to 'INVALID'")
            exit(1)
        print("Configuration valid")
        exit(0)
    main()
