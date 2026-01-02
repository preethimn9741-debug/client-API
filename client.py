import argparse
import json
import os
import time
import requests

DEFAULT_API_URL = "https://open.er-api.com/v6/latest/"
MAX_RETRIES = 3
TIMEOUT = 5


def get_api_url():
    if os.getenv("API_BASE_URL"):
        return os.getenv("API_BASE_URL")

    if os.path.exists("config.json"):
        try:
            with open("config.json") as f:
                data = json.load(f)
                return data["base_url"]
        except Exception:
            raise ValueError("Invalid config.json")

    print("config.json not found. Using default API URL.")
    return DEFAULT_API_URL


def fetch_rates(base_currency):
    url = get_api_url() + base_currency

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, timeout=TIMEOUT)

            if response.status_code != 200:
                raise Exception(f"HTTP {response.status_code}")

            return response.json()

        except Exception as e:
            if attempt == MAX_RETRIES:
                raise Exception("API request failed after retries")
            time.sleep(2)


def validate_args(args):
    if args.command == "convert":
        if not args.to or args.amount is None:
            raise ValueError("Missing required arguments")

        if not isinstance(args.amount, (int, float)):
            raise ValueError("Amount must be a number")

        if args.amount <= 0:
            raise ValueError("Amount must be positive")

    return True


def main():
    parser = argparse.ArgumentParser(description="REST API Client")
    subparsers = parser.add_subparsers(dest="command")

    rates = subparsers.add_parser("rates")
    rates.add_argument("--from", dest="base", required=True)

    convert = subparsers.add_parser("convert")
    convert.add_argument("--from", dest="base", required=True)
    convert.add_argument("--to", required=True)
    convert.add_argument("--amount", type=float, required=True)

    args = parser.parse_args()

    try:
        validate_args(args)
        data = fetch_rates(args.base)

        if args.command == "rates":
            print(data["rates"])

        elif args.command == "convert":
            rate = data["rates"].get(args.to)
            if not rate:
                raise ValueError("Invalid target currency")

            result = args.amount * rate
            print(f"{args.amount} {args.base} = {result} {args.to}")

        else:
            parser.print_help()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
    
    
    
