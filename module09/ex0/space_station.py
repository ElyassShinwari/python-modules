"""Exercise 0: Space Station Data.

Basic Pydantic model with Field validation.
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Pydantic model representing a space station's vital data."""

    station_id: str = Field(
        ..., min_length=3, max_length=10,
        description="Unique station identifier"
    )
    name: str = Field(
        ..., min_length=1, max_length=50,
        description="Station name"
    )
    crew_size: int = Field(
        ..., ge=1, le=20,
        description="Number of crew members"
    )
    power_level: float = Field(
        ..., ge=0.0, le=100.0,
        description="Power level percentage"
    )
    oxygen_level: float = Field(
        ..., ge=0.0, le=100.0,
        description="Oxygen level percentage"
    )
    last_maintenance: datetime = Field(
        ..., description="Date of last maintenance"
    )
    is_operational: bool = Field(
        default=True,
        description="Whether the station is operational"
    )
    notes: Optional[str] = Field(
        default=None, max_length=200,
        description="Optional notes about the station"
    )


def main() -> None:
    """Demonstrate SpaceStation validation with valid and invalid data."""
    print("Space Station Data Validation")
    print("=" * 40)

    # Create a valid space station
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-01-15T10:30:00",
    )
    status = "Operational" if station.is_operational else "Offline"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")

    # Attempt to create an invalid station (crew_size > 20)
    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Overloaded Station",
            crew_size=25,
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance="2024-03-01T08:00:00",
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
            # print(error["type"])
            # print(error["loc"])


if __name__ == "__main__":
    main()
