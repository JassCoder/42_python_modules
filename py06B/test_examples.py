# from typing import Any

# # ! practice for data processor 

# class AgeChecker:
    
#     def validate(self, data: Any) -> bool:
#         if isinstance(data, int):
#             return True
        
#         if isinstance(data, list):
#             return all(isinstance(age, int) for age in data)
        
#         return False


# checker = AgeChecker()

# print(checker.validate(20))
# print(checker.validate([18, 21]))
# print(checker.validate("twenty"))
# print(checker.validate([18, "X"]))

# ! for numeric ingestion
class ShoppingBasket:
    def __init__(self) -> None:
        self.items: list[str] = []
        
    def add(self, fruit: str | list[str]) -> None:
        if isinstance(fruit, list):
            fruits = fruit
        else:
            fruits = [fruit]
        for item in fruits:
            self.items.append(item)
        


basket = ShoppingBasket()

basket.add("apple")
basket.add(["banana", "mango"])
basket.add(["banana1", "mango1"])
basket.add([123, "mango"])

print(basket.items)