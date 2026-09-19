
def input_temperature(temp_str: str) -> int:
    number: int = int(temp_str)
    return number


def test_temperature() -> None:
    print("Input data is '25'")
    temp: int = input_temperature("25")
    print(f"Temperature is now {temp}°C")

    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print()
    test_temperature()
    print()
    print("All tests completed - program didn't crash!")
