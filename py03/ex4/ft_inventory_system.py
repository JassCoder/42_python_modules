import sys


c = "\033[32m"
r = "\033[0m"


def parse_inventory(argv):
    inventory = {}
    
    for arg in argv:
        if ':' not in arg:
            print(f"{c}Error - invalid parameter '{arg}'")
            continue
        
        name, value = arg.split(':', 1)
    


def main() -> None:
    inventory = parse_inventory(sys.argv[1:])
    print("=== Inventory System Analysis ===")
    print(f"{c}{inventory}{r}")


if __name__ == "__main__":
    main()
