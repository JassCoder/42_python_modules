import sys
""" value_check function is checking ->
the passing arguments are intergers(in the form of strings) or not
try if they integer(in the form of strings) than return converted int value
to list of number i created
"""


def value_check(args: list[str]) -> list[int]:
    numbers: list[int] = []
    for x in args:
        try:
            numbers.append(int(x))
        except ValueError:
            print(f"Invalid parameter: '{x}'")
            print("No scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1> <score2> ...")
            sys.exit(1)
    return numbers


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    int_numbers: list[int] = value_check(sys.argv[1:])
    if not int_numbers:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit(1)
    print(f"score processed : {int_numbers}")
    print(f"Total players : {len(sys.argv[1:])}")
    print(f"Total score : {sum(int_numbers)}")
    print(f"Average score : {sum(int_numbers) / len(int_numbers)}")
    print(f"Max score : {max(int_numbers)}")
    print(f"Min score : {min(int_numbers)}")
