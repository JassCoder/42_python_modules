"""Space crew and mission validation with nested Pydantic models."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Ranks available to crew members."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """A validated member of a space mission crew."""

    member_id: str = Field(
        ..., min_length=3, max_length=10, description="Unique crew member ID"
    )
    name: str = Field(
        ..., min_length=2, max_length=50, description="Crew member name"
    )
    rank: Rank = Field(..., description="Crew member rank")
    age: int = Field(
        ..., ge=18, le=80, description="Crew member age in years"
    )
    specialization: str = Field(
        ..., min_length=3, max_length=30, description="Area of expertise"
    )
    years_experience: int = Field(
        ..., ge=0, le=50, description="Years of experience"
    )
    is_active: bool = Field(
        default=True, description="Whether the member is active"
    )


class SpaceMission(BaseModel):
    """A validated space mission with its crew."""

    mission_id: str = Field(
        ..., min_length=5, max_length=15, description="Unique mission ID"
    )
    mission_name: str = Field(
        ..., min_length=3, max_length=100, description="Mission name"
    )
    destination: str = Field(
        ..., min_length=3, max_length=50, description="Mission destination"
    )
    launch_date: datetime = Field(
        ..., description="Scheduled launch date and time"
    )
    duration_days: int = Field(
        ..., ge=1, le=3650, description="Mission duration in days"
    )
    crew: list[CrewMember] = Field(
        ..., min_length=1, max_length=12, description="Mission crew"
    )
    mission_status: str = Field(
        default="planned", description="Current mission status"
    )
    budget_millions: float = Field(
        ..., ge=1.0, le=10000.0, description="Mission budget in millions"
    )

    @model_validator(mode="after")
    def validate_mission_safety(self) -> "SpaceMission":
        """Apply the observatory's mission safety requirements."""
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leadership_ranks = (Rank.COMMANDER, Rank.CAPTAIN)
        if not any(member.rank in leadership_ranks for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        if self.duration_days > 365:
            experienced_count = sum(
                1
                for member in self.crew
                if member.years_experience >= 5
            )
            if experienced_count * 2 < len(self.crew):
                raise ValueError(
                    "Long missions (> 365 days) require at least 50% "
                    "experienced crew (5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def first_error_message(error: ValidationError) -> str:
    """Return the first validation message without Pydantic's prefix."""
    message = str(error.errors()[0]["msg"])
    return message.removeprefix("Value error, ")


def main() -> None:
    """Demonstrate valid and invalid space mission crews."""
    print("Space Mission Crew Validation")
    print("=" * 41)

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2025, 3, 1, 9, 0),
        duration_days=900,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Rank.COMMANDER,
                age=45,
                specialization="Mission Command",
                years_experience=20,
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Rank.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=8,
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Rank.OFFICER,
                age=29,
                specialization="Engineering",
                years_experience=3,
            ),
        ],
        budget_millions=2500.0,
    )

    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions:.1f}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) "
            f"- {member.specialization}"
        )
    print("=" * 41)
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Unsafe Moon Mission",
            destination="Moon",
            launch_date=datetime(2025, 5, 1, 12, 0),
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Brown",
                    rank=Rank.OFFICER,
                    age=40,
                    specialization="Engineering",
                    years_experience=10,
                ),
                CrewMember(
                    member_id="CM005",
                    name="Eve Davis",
                    rank=Rank.CADET,
                    age=22,
                    specialization="Science",
                    years_experience=1,
                ),
            ],
            budget_millions=100.0,
        )
    except ValidationError as error:
        print(first_error_message(error))


if __name__ == "__main__":
    main()
