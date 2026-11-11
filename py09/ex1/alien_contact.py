from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator

class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


def main() -> None:
    print(ContactType.RADIO.value)


if __name__ == "__main__":
    main()