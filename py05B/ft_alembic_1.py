import alchemy


def main() -> None:
    print(alchemy.create_air())
    try:
        print(alchemy.create_earth())
    except AttributeError:
        print("create_earth() is not exposed by alchemy")


if __name__ == "__main__":
    main()