import sys

""" value_check function is checking -> the passing arguments are intergers(in the form of strings) or not
try if they integer(in the form of strings) than return converted int value 
to list of number i created
"""

def value_check(args: list[str]) -> list[int]:
    try:
        return [int(x) for x  in sys.argv[1:]]
    except ValueError:
        for argument in sys.argv[1:]:
            print(f"Invalid parameter: '{argument}'")
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit(1)


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    int_numbers: list[int] = value_check(sys.argv[1:])
    if not int_numbers:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit(1)
    print(f"score processed : {int_numbers}")
    print(f"Total players : {len(sys.argv[1:])}")
    print(f"Total score : {sum(int_numbers)}")
    print(f"Average score : {sum(int_numbers) / len(int_numbers)}")
    print(f"Max score : {max(sys.argv[1:])}")
    print(f"Min score : {min(sys.argv[1:])}")