"""Alien contact log validation with custom business rules."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Types of alien contact reported to the observatory."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """A validated report of contact with an alien species."""

    contact_id: str = Field(
        ..., min_length=5, max_length=15, description="Contact report ID"
    )
    timestamp: datetime = Field(..., description="Date and time of contact")
    location: str = Field(
        ..., min_length=3, max_length=100, description="Contact location"
    )
    contact_type: ContactType = Field(
        ..., description="Method of contact"
    )
    signal_strength: float = Field(
        ..., ge=0.0, le=10.0, description="Signal strength from 0 to 10"
    )
    duration_minutes: int = Field(
        ..., ge=1, le=1440, description="Contact duration in minutes"
    )
    witness_count: int = Field(
        ..., ge=1, le=100, description="Number of witnesses"
    )
    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Optional message received from the aliens",
    )
    is_verified: bool = Field(
        default=False, description="Whether the report has been verified"
    )

    @model_validator(mode="after")
    def validate_business_rules(self) -> "AlienContact":
        """Apply the observatory's contact reporting rules."""
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if (
            self.contact_type is ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) must include a received message"
            )

        return self


def first_error_message(error: ValidationError) -> str:
    """Return the first validation message without Pydantic's prefix."""
    message = str(error.errors()[0]["msg"])
    return message.removeprefix("Value error, ")


def main() -> None:
    """Demonstrate valid and invalid alien contact reports."""
    print("Alien Contact Log Validation")
    print("=" * 38)

    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 6, 12, 21, 45),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )

    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")
    print("=" * 38)
    print("Expected validation error:")

    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 6, 13, 3, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.0,
            duration_minutes=10,
            witness_count=2,
        )
    except ValidationError as error:
        print(first_error_message(error))


if __name__ == "__main__":
    main()
