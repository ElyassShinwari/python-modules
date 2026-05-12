"""Alien Contact Logs - Custom validation with @model_validator."""

from datetime import datetime
from enum import Enum
from typing import Optional
# import json

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Types of alien contact encounters."""

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model for alien contact reports with custom validation."""

    contact_id: str = Field(
        ..., min_length=5, max_length=15,
        description="Unique contact report identifier"
    )
    timestamp: datetime = Field(
        ..., description="Date and time of contact"
    )
    location: str = Field(
        ..., min_length=3, max_length=100,
        description="Location of the contact"
    )
    contact_type: ContactType = Field(
        ..., description="Type of contact"
    )
    signal_strength: float = Field(
        ..., ge=0.0, le=10.0,
        description="Signal strength on 0-10 scale"
    )
    duration_minutes: int = Field(
        ..., ge=1, le=1440,
        description="Duration in minutes (max 24 hours)"
    )
    witness_count: int = Field(
        ..., ge=1, le=100,
        description="Number of witnesses"
    )
    message_received: Optional[str] = Field(
        default=None, max_length=500,
        description="Optional message content"
    )
    is_verified: bool = Field(
        default=False,
        description="Whether the contact is verified"
    )

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Apply custom business rules for contact reports."""
        # Contact ID must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                'Contact ID must start with "AC"'
            )
        # Physical contact reports must be verified
        if (
            self.contact_type == ContactType.PHYSICAL
            and not self.is_verified
        ):
            raise ValueError(
                "Physical contact reports must be verified"
            )
        # Telepathic contact requires at least 3 witnesses
        if (
            self.contact_type == ContactType.TELEPATHIC
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )
        # Strong signals (> 7.0) should include received messages
        if (
            self.signal_strength > 7.0
            and not self.message_received
        ):
            raise ValueError(
                "Strong signals (> 7.0) should include a message"
            )
        return self


# def json_reader():
#     with open("ac.json", "r", encoding="utf-8") as file:
#         data = json.load(file)
#         # # lst: list = []
#         # for _ in data:
#         # #     lst.append(_)
#         #     print(_, "\n")

#     return data


def main() -> None:
    """Demonstrate AlienContact validation with valid and invalid data."""
    print("Alien Contact Log Validation")
    print("=" * 40)

    # Create a valid contact report
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime.fromisoformat("2024-06-15T03:45:00"),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
    )
    # contacts = json_reader()
    # numb: int = 1
    # contact = AlienContact(
    #     contact_id=contacts[numb]["contact_id"],
    #     timestamp=contacts[numb]["timestamp"],
    #     location=contacts[numb]["location"],
    #     contact_type=contacts[numb]["contact_type"],
    #     signal_strength=contacts[numb]["signal_strength"],
    #     duration_minutes=contacts[numb]["duration_minutes"],
    #     witness_count=contacts[numb]["witness_count"],
    #     message_received=contacts[numb]["message_received"],
    # )
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: '{contact.message_received}'")

    # Attempt invalid: telepathic with only 1 witness
    print()
    print("=" * 40)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.fromisoformat("2024-07-01T12:00:00"),
            location="Roswell, New Mexico",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=3.0,
            duration_minutes=10,
            witness_count=1,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])
            # print(error["type"])
            # print(error["loc"])


if __name__ == "__main__":
    main()
