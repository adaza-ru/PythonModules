import os
import sys
from dotenv import load_dotenv


def check_security():
    """Realiza una comprobación simulada de seguridad del entorno."""
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file is missing")

    print("[OK] Production overrides available")


def main():
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    missing_configs = []
    if not mode:
        missing_configs.append("MATRIX_MODE")
    if not db_url:
        missing_configs.append("DATABASE_URL")
    if not api_key:
        missing_configs.append("API_KEY")
    if not log_level:
        missing_configs.append("LOG_LEVEL")
    if not zion_endpoint:
        missing_configs.append("ZION_ENDPOINT")

    if missing_configs:
        print("\n[WARNING] Missing configuration detected. "
              "Defaulting to safe mode/warnings:")
        for config in missing_configs:
            print(f"  -> '{config}' is not set.")
        print("\nPlease ensure you have copied .env.example "
              "to .env and filled out the values,")
        print(
            "or that you are passing them directly as environment variables."
        )
        sys.exit(1)

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")

    if mode.lower() == "production":
        print("Database: Connected to PRODUCTION secure instance")
        print("API Access: Authenticated via Production Gateway")
        print(f"Log Level: {log_level}")
        print("Zion Network: SECURE UPLINK ESTABLISHED")
    else:
        print("Database: Connected to local development instance")
        print("API Access: Authenticated via Sandbox Gateway")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online (Local Simulation)")

    print()
    check_security()

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
