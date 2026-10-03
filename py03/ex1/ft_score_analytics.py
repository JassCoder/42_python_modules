import sys


def value_check(args: list[str]) -> list[int]:
    numbers: list[int] = []
    for x in args:
        try:
            numbers.append(int(x))
        except ValueError:
            print(f"Invalid parameter: '{x}'")
    return numbers


def main() -> None:
    print("=== Player Score Analytics ===")
    int_numbers: list[int] = value_check(sys.argv[1:])

    if not int_numbers:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        sys.exit(1)

    print(f"Scores processed: {int_numbers}")
    print(f"Total players: {len(int_numbers)}")
    print(f"Total score: {sum(int_numbers)}")
    print(f"Average score: {sum(int_numbers) / len(int_numbers)}")
    print(f"High score: {max(int_numbers)}")
    print(f"Low score: {min(int_numbers)}")
    print(f"Score range: {max(int_numbers) - min(int_numbers)}")


if __name__ == "__main__":
    main()
