
def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        10 / 0
    elif operation_number == 2:
        open("non/existent/file")
    elif operation_number == 3:
        "garden" + 42
    else:
        return


def test_error_types() -> None:
    for operation_number in range(5):
        print(f"Testing operation {operation_number}...")

        try:
            garden_operations(operation_number)

            if operation_number == 4:
                print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    print()
    print("=== Garden Error Types Demo ===")
    test_error_types()
