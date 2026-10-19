"""Space station data validation using Pydantic models."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Validated data reported by a space station."""

    station_id: str = Field(
        ..., min_length=3, max_length=10, description="Unique station ID"
    )
    name: str = Field(
        ..., min_length=1, max_length=50, description="Station name"
    )
    crew_size: int = Field(
        ..., ge=1, le=20, description="Number of people on board"
    )
    power_level: float = Field(
        ..., ge=0.0, le=100.0, description="Power level in percent"
    )
    oxygen_level: float = Field(
        ..., ge=0.0, le=100.0, description="Oxygen level in percent"
    )
    last_maintenance: datetime = Field(
        ..., description="Date and time of the last maintenance"
    )
    is_operational: bool = Field(
        default=True, description="Whether the station is operational"
    )
    notes: Optional[str] = Field(
        default=None, max_length=200, description="Optional station notes"
    )


def first_error_message(error: ValidationError) -> str:
    """Return the first validation message without Pydantic's prefix."""
    message = str(error.errors()[0]["msg"])
    return message.removeprefix("Value error, ")


def main() -> None:
    """Demonstrate valid and invalid space station data."""
    print("Space Station Data Validation")
    print("=" * 40)

    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 8, 30),
        notes="All systems nominal.",
    )

    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Offline"
    print(f"Status: {status}")
    print("=" * 40)
    print("Expected validation error:")

    try:
        SpaceStation(
            station_id="ISS002",
            name="Overcrowded Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=50.0,
            last_maintenance=datetime(2024, 1, 15, 8, 30),
        )
    except ValidationError as error:
        print(first_error_message(error))


if __name__ == "__main__":
    main()
