# ! practice for data processor
from typing import Any


class AgeChecker:

    def validate(self, data: Any) -> bool:
        if isinstance(data, int) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                isinstance(age, int) and not isinstance(age, bool)
                for age in data
            )
        return False


checker = AgeChecker()

print(checker.validate(20))          # True
print(checker.validate([18, 21]))    # True
print(checker.validate("twenty"))    # False
print(checker.validate([18, "X"]))   # False
print(checker.validate(True))        # False (with the bool guard)


# ! for text ingestion (basket of fruit names)
class ShoppingBasket:

    def __init__(self) -> None:
        self.items: list[str] = []

    def validate(self, data: str | list[str]) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)
        return False

    def add(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("invalid input")
        fruits = data if isinstance(data, list) else [data]
        self.items.extend(fruits)


basket = ShoppingBasket()

basket.add("apple")
basket.add(["banana", "mango"])
basket.add(["banana1", "mango1"])

print(basket.items)
# ['apple', 'banana', 'mango', 'banana1', 'mango1']
