from __future__ import annotations
from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):

    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

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
    def validate_business_rules(self) -> AlienContact:
        """
        Applies complex business logic after individual fields are validated.
        """
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        is_telepathic: bool = self.contact_type == ContactType.TELEPATHIC

        if is_telepathic and self.witness_count < 3:
            raise ValueError("Telepathic contact requires "
                             "at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def display_report(report: AlienContact) -> None:

    print(f"ID: {report.contact_id}")
    print(f"Type: {report.contact_type.value}")
    print(f"Location: {report.location}")
    print(f"Signal: {report.signal_strength}/10")
    print(f"Duration: {report.duration_minutes} minutes")
    print(f"Witnesses: {report.witness_count}")
    if report.message_received:
        print(f"Message: '{report.message_received}'")


def main() -> None:

    print("Alien Contact Log Validation")
    print("=" * 40)

    try:
        valid_radio: AlienContact = AlienContact(
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

    print("\n" + "=" * 40)
    print("Expected validation errors:\n")

    try:

        wrong_radio_1: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Wrong contact failed to fail.")
        display_report(wrong_radio_1)
    except ValidationError as e:
        for error in e.errors():
            msg = error['msg'].replace('Value error, ', '')
            print(msg)

    try:
        wrong_radio_2: AlienContact = AlienContact(
            contact_id="BC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Wrong contact failed to fail.")
        display_report(wrong_radio_2)
    except ValidationError as e:
        for error in e.errors():
            msg = error['msg'].replace('Value error, ', '')
            print(msg)

    try:
        wrong_radio_3: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.PHYSICAL,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print("Wrong contact failed to fail.")
        display_report(wrong_radio_3)
    except ValidationError as e:
        for error in e.errors():
            msg = error['msg'].replace('Value error, ', '')
            print(msg)

    try:
        wrong_radio_4: AlienContact = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5
        )
        print("Wrong contact failed to fail.")
        display_report(wrong_radio_4)
    except ValidationError as e:
        for error in e.errors():
            msg = error['msg'].replace('Value error, ', '')
            print(msg)


if __name__ == "__main__":
    main()
