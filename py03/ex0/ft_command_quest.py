import sys

if __name__ == "__main__":

    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        for i, argument in enumerate(sys.argv[1:], 1):
            print(f"Argument {i}: {argument}")
    print(f"Total arguments: {len(sys.argv)}")
