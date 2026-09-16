#!/usr/bin/env python3

"""
Helper file for Growing Code.

Run:
    python3 main.py

Expected structure:

py00/
├── main.py
├── ex0/
│   └── ft_hello_garden.py
├── ex1/
│   └── ft_garden_name.py
├── ex2/
│   └── ft_plot_area.py
├── ex3/
│   └── ft_harvest_total.py
├── ex4/
│   └── ft_plant_age.py
├── ex5/
│   └── ft_water_reminder.py
├── ex6/
│   ├── ft_count_harvest_iterative.py
│   └── ft_count_harvest_recursive.py
└── ex7/
    └── ft_seed_inventory.py
"""


def test_ft_exercise(exercise_number, exercise_file_name):
    """Import and test one exercise."""
    print(f"\n=== Testing ex{exercise_number}/{exercise_file_name} ===")

    try:
        import sys

        sys.path.append(".")

        # Example:
        # ex0.ft_hello_garden
        # ex6.ft_count_harvest_recursive
        module_name = f"ex{exercise_number}.{exercise_file_name}"

        ft_module = __import__(
            module_name,
            fromlist=[exercise_file_name]
        )

        ft_function = getattr(ft_module, exercise_file_name)

        # Exercise 7 takes parameters
        if exercise_file_name == "ft_seed_inventory":
            print("Testing with different seed types and units:\n")

            ft_function("tomato", 15, "packets")
            ft_function("carrot", 8, "grams")
            ft_function("lettuce", 12, "area")

            print("\nTesting with unknown unit:")
            ft_function("basil", 5, "unknown")

        else:
            # Exercises 0-6 take no parameters
            ft_function()

    except ImportError as error:
        print(
            f"❌ Could not import "
            f"ex{exercise_number}/{exercise_file_name}.py"
        )
        print(f"   Import error: {error}")

    except AttributeError:
        print(
            f"❌ Could not find function "
            f"{exercise_file_name}()"
        )
        print(
            f"   Check ex{exercise_number}/"
            f"{exercise_file_name}.py"
        )

    except TypeError as error:
        msg = str(error)

        print(f"❌ Type error: {error}")

        if exercise_file_name == "ft_seed_inventory":
            if "missing" in msg and "required positional argument" in msg:
                print(
                    "   Exercise 7 should take parameters:"
                )
                print(
                    "   def ft_seed_inventory("
                    "seed_type: str, "
                    "quantity: int, "
                    "unit: str"
                    ") -> None:"
                )
        else:
            print(
                "   This function should not take any parameters"
            )

    except Exception as error:
        print(f"❌ Error running your function: {error}")


def main():
    """Run the exercise tester."""
    print("🌱 Welcome to Growing Code! 🌱")
    print("This helper will test your exercises.")
    print()

    print("0 - ft_hello_garden")
    print("1 - ft_garden_name")
    print("2 - ft_plot_area")
    print("3 - ft_harvest_total")
    print("4 - ft_plant_age")
    print("5 - ft_water_reminder")
    print("6 - ft_count_harvest")
    print("7 - ft_seed_inventory")
    print("a - test all exercises")
    print()

    choice = input("Enter your choice: ")

    if choice == "0":
        test_ft_exercise(0, "ft_hello_garden")

    elif choice == "1":
        test_ft_exercise(1, "ft_garden_name")

    elif choice == "2":
        test_ft_exercise(2, "ft_plot_area")

    elif choice == "3":
        test_ft_exercise(3, "ft_harvest_total")

    elif choice == "4":
        test_ft_exercise(4, "ft_plant_age")

    elif choice == "5":
        test_ft_exercise(5, "ft_water_reminder")

    elif choice == "6":
        test_ft_exercise(
            6,
            "ft_count_harvest_iterative"
        )
        test_ft_exercise(
            6,
            "ft_count_harvest_recursive"
        )

    elif choice == "7":
        test_ft_exercise(7, "ft_seed_inventory")

    elif choice == "a":
        test_ft_exercise(0, "ft_hello_garden")
        test_ft_exercise(1, "ft_garden_name")
        test_ft_exercise(2, "ft_plot_area")
        test_ft_exercise(3, "ft_harvest_total")
        test_ft_exercise(4, "ft_plant_age")
        test_ft_exercise(5, "ft_water_reminder")

        test_ft_exercise(
            6,
            "ft_count_harvest_iterative"
        )
        test_ft_exercise(
            6,
            "ft_count_harvest_recursive"
        )

        test_ft_exercise(7, "ft_seed_inventory")

    else:
        print(
            "❌ Invalid choice! "
            "Enter 0, 1, 2, 3, 4, 5, 6, 7, or a"
        )


if __name__ == "__main__":
    main()