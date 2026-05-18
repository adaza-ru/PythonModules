from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(default=None, max_length=200)


def display_station(station: SpaceStation) -> None:

    status: str = "Operational" if station.is_operational else "Offline"
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")


def main() -> None:

    print("Space Station Data Validation")
    print("=" * 40)

    try:
        valid_station: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now()
        )
        print("Valid station created:")
        display_station(valid_station)

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("\n" + "=" * 40)
    print("Expected validation error:")

    try:
        wrong_station: SpaceStation = SpaceStation(
            station_id="IS",
            name="",
            crew_size=25,
            power_level=150.0,
            oxygen_level=145.0,
            last_maintenance=datetime.now()
        )
        print("Wrong station failed to fail.")
        display_station(wrong_station)
    except ValidationError as e:
        for error in e.errors():
            print(f"Error in {error['loc'][0]}: {error['msg']}")


if __name__ == "__main__":
    main()
