def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def helper(day, max_days):
        if day > max_days:
            return
        print(f"Day {day}")
        helper(day + 1, max_days)
    helper(1, n)
    print("Harvest time!")
