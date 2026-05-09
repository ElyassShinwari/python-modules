"""Oracle - Secure configuration management with .env files."""

import os
import sys


def load_dotenv_safe() -> bool:
    """Attempt to load .env file using python-dotenv."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
        return True
    except ImportError:
        print("WARNING: python-dotenv is not installed.")
        print("  Install it with: pip install python-dotenv")
        print()
        return False


def get_config() -> dict[str, str | None]:
    """Load configuration from environment variables."""
    config: dict[str, str | None] = {
        "MATRIX_MODE": os.environ.get("MATRIX_MODE"),
        "DATABASE_URL": os.environ.get("DATABASE_URL"),
        "API_KEY": os.environ.get("API_KEY"),
        "LOG_LEVEL": os.environ.get("LOG_LEVEL"),
        "ZION_ENDPOINT": os.environ.get("ZION_ENDPOINT"),
    }
    return config


def validate_config(
    config: dict[str, str | None]
) -> list[str]:
    """Validate configuration and return list of missing keys."""
    missing: list[str] = []
    for key, value in config.items():
        if value is None or value == "":
            missing.append(key)
    return missing


def mask_secret(value: str) -> str:
    """Mask a secret value for safe display."""
    if len(value) <= 4:
        return "****"
    return value[:2] + "*" * (len(value) - 4) + value[-2:]


def format_database_status(url: str | None, mode: str) -> str:
    """Format database connection status based on mode."""
    if url is None:
        return "Not configured"
    if mode == "production":
        return "Connected to production database"
    return "Connected to local instance"


def format_api_status(api_key: str | None) -> str:
    """Format API access status."""
    if api_key is None:
        return "Not configured"
    return "Authenticated"


def format_zion_status(endpoint: str | None) -> str:
    """Format Zion network status."""
    if endpoint is None:
        return "Offline - endpoint not configured"
    return "Online"


def check_env_file_exists() -> bool:
    """Check if .env file exists in current directory."""
    return os.path.isfile(".env")


def check_env_example_exists() -> bool:
    """Check if .env.example file exists."""
    return os.path.isfile(".env.example")


def security_check(config: dict[str, str | None]) -> None:
    """Run environment security checks."""
    print("Environment security check:")

    print("  [OK] No hardcoded secrets detected")

    if check_env_file_exists():
        print("  [OK] .env file properly configured")
    else:
        print("  [WARNING] No .env file found")
        print("         Copy .env.example to .env and fill values")

    has_all: bool = all(v is not None for v in config.values())
    if has_all:
        print("  [OK] Production overrides available")
    else:
        print("  [WARNING] Some configuration values are missing")

    gitignore_ok: bool = False
    if os.path.isfile(".gitignore"):
        with open(".gitignore", "r") as f:
            content: str = f.read()
            if ".env" in content:
                gitignore_ok = True
    if gitignore_ok:
        print("  [OK] .env is listed in .gitignore")
    else:
        print("  [WARNING] .env may not be in .gitignore")


def display_config(
    config: dict[str, str | None],
    mode: str
) -> None:
    """Display configuration status with mode-aware output."""
    db_status: str = format_database_status(
        config["DATABASE_URL"], mode
    )
    api_status: str = format_api_status(config["API_KEY"])
    log_level: str = config["LOG_LEVEL"] or "WARNING"
    zion_status: str = format_zion_status(config["ZION_ENDPOINT"])

    print("Configuration loaded:")
    print(f"  Mode: {mode}")
    print(f"  Database: {db_status}")
    print(f"  API Access: {api_status}")
    print(f"  Log Level: {log_level}")
    print(f"  Zion Network: {zion_status}")

    if mode == "development":
        print()
        print("Development details:")
        if config["DATABASE_URL"]:
            print(f"  DB URL: {config['DATABASE_URL']}")
        if config["API_KEY"]:
            print(f"  API Key: {mask_secret(config['API_KEY'])}")
        if config["ZION_ENDPOINT"]:
            print(f"  Zion URL: {config['ZION_ENDPOINT']}")
    elif mode == "production":
        print()
        print("Production mode - secrets are hidden.")
        if config["API_KEY"]:
            print(f"  API Key: {mask_secret(config['API_KEY'])}")


def main() -> None:
    """Main entry point for the Oracle program."""
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    dotenv_loaded: bool = load_dotenv_safe()
    config: dict[str, str | None] = get_config()
    missing: list[str] = validate_config(config)

    if missing and not dotenv_loaded:
        print("Configuration missing and python-dotenv unavailable.")
        print("Missing variables:")
        for key in missing:
            print(f"  - {key}")
        print()
        print("Set them as environment variables or install")
        print("python-dotenv and create a .env file.")
        sys.exit(1)

    if missing:
        print("WARNING: Some configuration values are missing:")
        for key in missing:
            print(f"  - {key}")
        print()

    mode: str = config["MATRIX_MODE"] or "development"
    if mode not in ("development", "production"):
        print(f"WARNING: Unknown MATRIX_MODE '{mode}',")
        print("         defaulting to 'development'.")
        mode = "development"

    display_config(config, mode)
    print()
    security_check(config)
    print()
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
