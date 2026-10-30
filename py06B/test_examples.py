from typing import Any

class AgeChecker:
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, int):
            return True
        
        if isinstance(data, list):
            return all(isinstance(age, int) for age in data)
        
        return False


checker = AgeChecker()

print(checker.validate(20))
print(checker.validate([18, 21]))
print(checker.validate("twenty"))
print(checker.validate([18, "X"]))