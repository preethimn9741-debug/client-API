import requests


def validate_args(args):
    """
    Validate command-line arguments for currency conversion
    """

    if args.command != "convert":
        raise ValueError("Invalid command")

    if not args.to or not isinstance(args.to, str):
        raise ValueError("Target currency must be a string")

    if len(args.to) != 3 or not args.to.isalpha():
        raise ValueError("Invalid currency code")

    if args.amount is None:
        raise ValueError("Amount is required")

    if not isinstance(args.amount, (int, float)):
        raise ValueError("Amount must be a number")

    if args.amount <= 0:
        raise ValueError("Amount must be greater than zero")

    return True


def fetch_rates(base_currency):
    """
    Fetch exchange rates from external API
    """

    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    except Exception as e:
        raise Exception("Failed to fetch exchange rates") from e


# ==================================================
# RUNNABLE ENTRY POINT (does NOT affect test cases)
# ==================================================

if __name__ == "__main__":

    class Args:
        def __init__(self, command, to, amount):
            self.command = command
            self.to = to
            self.amount = amount

    # Sample input (can be changed)
    args = Args("convert", "INR", 10)

    try:
        # Validate input
        validate_args(args)

        # Fetch rates
        data = fetch_rates("USD")

        # Calculate conversion
        rate = data["rates"].get(args.to)
        if rate is None:
            raise ValueError("Currency not found in response")

        converted_amount = args.amount * rate

        print("Conversion Successful")
        print(f"{args.amount} USD = {converted_amount} {args.to}")

    except Exception as e:
        print("Error:", e)

