# ANSI escape codes for some common colors
class Console_Colors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'  # Resets the color to default

if __name__ == '__main__':
    # Using the colors
    print(f"{Console_Colors.RED}This will be red{Console_Colors.RESET}")
    print(f"{Console_Colors.GREEN}This will be green{Console_Colors.RESET}")
    print(f"{Console_Colors.BLUE}This will be blue{Console_Colors.RESET}")
    print(f"{Console_Colors.MAGENTA}This is called magenta, but it's pink 😁{Console_Colors.RESET}")
