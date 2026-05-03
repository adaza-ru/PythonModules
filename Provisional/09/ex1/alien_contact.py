from enum import Enum
from datetime import datetime
from typing import Optional, Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Supported types of alien contact."""
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    """
    Model representing an alien contact report with cross-field validation.
    """
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_business_rules(self) -> Self:
        """
        Applies complex business logic after individual fields are validated.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def display_report(report: AlienContact) -> None:
    """Prints a contact report in a clean format."""
    print(f"ID: {report.contact_id}")
    print(f"Type: {report.contact_type.value}")
    print(f"Location: {report.location}")
    print(f"Signal: {report.signal_strength}/10")
    print(f"Duration: {report.duration_minutes} minutes")
    print(f"Witnesses: {report.witness_count}")
    if report.message_received:
        print(f"Message: '{report.message_received}'")


def main() -> None:
    """Demonstrates validation of alien contact reports."""
    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        valid_radio = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Valid contact report:")
        display_report(valid_radio)

    except ValidationError as e:
        print(f"Unexpected error in valid case: {e}")

    print("=" * 40)
    print("Expected validation errors:")

    try:
        AlienContact(
            contact_id="AC_TELE_99",
            timestamp=datetime.now(),
            location="Remote Woods",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=2.0,
            duration_minutes=10,
            witness_count=1
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"- {error['msg']}")

    try:
        AlienContact(
            contact_id="AC_SIGNAL_X",
            timestamp=datetime.now(),
            location="Satellite Dish A1",
            contact_type=ContactType.RADIO,
            signal_strength=9.9,
            duration_minutes=5,
            witness_count=2
        )
    except ValidationError as e:
        for error in e.errors():
            print(f"- {error['msg']}")


if __name__ == "__main__":
    main()
