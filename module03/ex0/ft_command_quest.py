import sys


def main() -> None:
    """Command Quest: displays command-line arguments."""
    print("=== Command Quest ===")
    args: list = sys.argv
    if len(args) == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print(f"Total arguments: {len(args)}")
    else:
        print(f"Program name: {args[0]}")
        print(f"Argument received: {len(args) - 1}")
        i: int = 1
        while i < len(args):
            print(f"Argument {i}: {args[i]}")
            i = i + 1
        print(f"Total arguments: {len(args)}")


if __name__ == "__main__":
    main()
