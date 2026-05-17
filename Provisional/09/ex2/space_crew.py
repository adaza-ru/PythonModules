from enum import Enum
from datetime import datetime
from typing import List, Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Crew ranks available for mission assignment."""
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    """
    Model representing an individual crew member.
    """
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    """
    Model representing a space mission with nested crew validation.
    """
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_mission_safety(self) -> Self:
        """
        Applies mission-wide safety requirements and crew composition rules.
        """
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        leaders = {Rank.COMMANDER, Rank.CAPTAIN}
        has_leader = any(member.rank in leaders for member in self.crew)
        if not has_leader:
            raise ValueError("Mission must have at least "
                             "one Commander or Captain")

        if self.duration_days > 365:
            experienced_count = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced_count < (len(self.crew) / 2):
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )

        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")

        return self


def display_mission(mission: SpaceMission) -> None:
    """Displays mission and crew details formatted clearly."""
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for m in mission.crew:
        print(f"- {m.name} ({m.rank.value}) - {m.specialization}")


def main() -> None:
    """Demonstrates valid and invalid space mission scenarios."""
    print("Space Mission Crew Validation")
    print("=" * 41)

    try:
        valid_mission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2024-10-12T08:00:00",
            duration_days=900,
            budget_millions=2500.0,
            crew=[
                CrewMember(
                    member_id="C01", name="Sarah Connor", rank=Rank.COMMANDER,
                    age=45, specialization="Mission Command",
                    years_experience=15
                ),
                CrewMember(
                    member_id="C02", name="John Smith", rank=Rank.LIEUTENANT,
                    age=30, specialization="Navigation", years_experience=6
                ),
                CrewMember(
                    member_id="C03", name="Alice Johnson", rank=Rank.OFFICER,
                    age=28, specialization="Engineering", years_experience=2
                )
            ]
        )
        print("Valid mission created:")
        display_mission(valid_mission)

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 41)
    print("Expected validation error:")

    try:
        SpaceMission(
            mission_id="M_FAIL_01",
            mission_name="Unmanned Test?",
            destination="Moon",
            launch_date=datetime.now(),
            duration_days=10,
            budget_millions=100.0,
            crew=[
                CrewMember(
                    member_id="C04", name="Newbie", rank=Rank.CADET,
                    age=19, specialization="Cleaning", years_experience=0
                )
            ]
        )
    except ValidationError as e:
        for error in e.errors():
            print(error['msg'])


if __name__ == "__main__":
    main()
