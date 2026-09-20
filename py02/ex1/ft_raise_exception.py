
def input_temperature(temp_str: str) -> int:
    number: int = int(temp_str)
    if number > 40:
        raise ValueError(
            f"{number}°C is too hot for plants (max 40°C)"
        )
    if number < 0:
        raise ValueError(
            f"{number}°C is too cold for plants (min 0°C)"
        )
    return number


def test_temperature() -> None:
    print("Input data is '25'")
    temp: int = input_temperature("25")
    print(f"Temperature is now {temp}°C")
    print()
    print()
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print()
    print("Input data is '100'")
    try:
        input_temperature("100")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print("")
    print("")
    print("Input data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
