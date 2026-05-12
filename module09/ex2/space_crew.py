"""Space Crew Management - Nested models and complex validation."""

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Crew member ranks."""

    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """Pydantic model for an individual crew member."""

    member_id: str = Field(
        ..., min_length=3, max_length=10,
        description="Unique member identifier"
    )
    name: str = Field(
        ..., min_length=2, max_length=50,
        description="Full name of the crew member"
    )
    rank: Rank = Field(
        ..., description="Crew rank"
    )
    age: int = Field(
        ..., ge=18, le=80,
        description="Age in years"
    )
    specialization: str = Field(
        ..., min_length=3, max_length=30,
        description="Area of specialization"
    )
    years_experience: int = Field(
        ..., ge=0, le=50,
        description="Years of experience"
    )
    is_active: bool = Field(
        default=True,
        description="Whether the member is active"
    )


class SpaceMission(BaseModel):
    """Pydantic model for a space mission with nested crew members."""

    mission_id: str = Field(
        ..., min_length=5, max_length=15,
        description="Unique mission identifier"
    )
    mission_name: str = Field(
        ..., min_length=3, max_length=100,
        description="Name of the mission"
    )
    destination: str = Field(
        ..., min_length=3, max_length=50,
        description="Mission destination"
    )
    launch_date: datetime = Field(
        ..., description="Planned launch date"
    )
    duration_days: int = Field(
        ..., ge=1, le=3650,
        description="Mission duration in days (max 10 years)"
    )
    crew: List[CrewMember] = Field(
        ..., min_length=1, max_length=12,
        description="List of crew members"
    )
    mission_status: str = Field(
        default="planned",
        description="Current mission status"
    )
    budget_millions: float = Field(
        ..., ge=1.0, le=10000.0,
        description="Budget in millions of dollars"
    )

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Apply mission safety and operational requirements."""
        # Mission ID must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError(
                'Mission ID must start with "M"'
            )
        # Must have at least one Commander or Captain
        has_leader = any(
            member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
            for member in self.crew
        )
        if not has_leader:
            raise ValueError(
                "Mission must have at least one "
                "Commander or Captain"
            )
        # Long missions (> 365 days) need 50% experienced crew
        if self.duration_days > 365:
            experienced = sum(
                1 for m in self.crew
                if m.years_experience >= 5
            )
            total = len(self.crew)
            if experienced < total / 2:
                raise ValueError(
                    "Long missions (> 365 days) require "
                    "at least 50% experienced crew (5+ years)"
                )
        # All crew members must be active
        inactive = [
            m.name for m in self.crew if not m.is_active
        ]
        if inactive:
            raise ValueError(
                "All crew members must be active. "
                f"Inactive: {', '.join(inactive)}"
            )
        return self


def main() -> None:
    """Demonstrate SpaceMission validation with valid and invalid data."""
    print("Space Mission Crew Validation")
    print("=" * 40)

    # Define crew members for a valid mission
    crew = [
        CrewMember(
            member_id="SC001",
            name="Sarah Connor",
            rank=Rank.COMMANDER,
            age=45,
            specialization="Mission Command",
            years_experience=20,
        ),
        CrewMember(
            member_id="SC002",
            name="John Smith",
            rank=Rank.LIEUTENANT,
            age=35,
            specialization="Navigation",
            years_experience=10,
        ),
        CrewMember(
            member_id="SC003",
            name="Alice Johnson",
            rank=Rank.OFFICER,
            age=28,
            specialization="Engineering",
            years_experience=6,
        ),
    ]

    # Create a valid mission
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime.fromisoformat("2024-12-01T06:00:00"),
        duration_days=900,
        crew=crew,
        budget_millions=2500.0,
    )
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"  - {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )

    # Attempt invalid: no Commander or Captain
    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        no_leader_crew = [
            CrewMember(
                member_id="SC010",
                name="Bob Ross",
                rank=Rank.CADET,
                age=22,
                specialization="Painting",
                years_experience=1,
            ),
        ]
        SpaceMission(
            mission_id="M2024_FAIL",
            mission_name="Doomed Mission",
            destination="Venus",
            launch_date=datetime.fromisoformat("2024-06-01T12:00:00"),
            duration_days=30,
            crew=no_leader_crew,
            budget_millions=100.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()
