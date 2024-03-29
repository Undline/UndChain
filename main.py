import argparse
from typing import Optional, Any

def check_system_key() -> bool:
    """
    Checks if a valid system key is present. Currently returns True as a placeholder.

    Returns:
        bool: True if a valid key is found, False otherwise.
    """
    # Placeholder for actual key checking logic
    return True

def main(user_type: Optional[str] = None, **kwargs: Any) -> None:
    """
    Main function that handles user type selection and additional keyword arguments.
    Continues to prompt for user type until 'exit' is entered.

    Args:
        user_type (Optional[str]): The type of user (Validator, Chain Owner, Partner, Client).
        **kwargs (Any): Additional keyword arguments for future use.

    """
    if not check_system_key():
        print("No valid system key found.")
        return

    while True:
        if user_type is None:
            user_input = input("Please enter your user type (Validator, Chain Owner, Partner, Client) or type 'exit' to quit: ").upper()

            if user_input == 'EXIT':
                print("Exiting UndChain.")
                break

            if user_input in ['VALIDATOR', 'CHAIN OWNER', 'PARTNER', 'CLIENT']:
                print(f"You are a {user_input.title()}. Still developing the role, so nothing happens after this.")
                # Specific user type code here
                break
            else:
                print("Invalid user type.")
        else:
            user_input = user_type.upper()
            if user_input in ['VALIDATOR', 'CHAIN OWNER', 'PARTNER', 'CLIENT']:
                print(f"You are a {user_input.title()}.")
                # Specific user type code here
            break  # Exit loop if user_type is provided as an argument

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="User type selection for UndChain")
    parser.add_argument("--user_type", type=str, help="Specify the user type (Validator, Chain Owner, Partner, Client)")

    args = parser.parse_args()

    main(user_type=args.user_type)
