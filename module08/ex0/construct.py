"""Construct - Virtual environment detection and information."""

import sys
import os
import site


def get_venv_name(venv_path: str) -> str:
    """Extract the virtual environment name from its path."""
    return os.path.basename(venv_path)


def get_package_path() -> str:
    """Get the site-packages installation path."""
    packages: list[str] = site.getsitepackages()
    if packages:
        return packages[0]
    return "Unknown"


def show_outside_matrix() -> None:
    """Display information when outside a virtual environment."""
    print("MATRIX STATUS: You're still plugged in")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print()
    print("To enter the construct, run:")
    print("  python -m venv matrix_env")
    print("  source matrix_env/bin/activate  # On Unix")
    print("  matrix_env\\Scripts\\activate    # On Windows")
    print()
    print("Then run this program again.")


def show_inside_construct(venv_path: str) -> None:
    """Display information when inside a virtual environment."""
    venv_name: str = get_venv_name(venv_path)
    package_path: str = get_package_path()

    print("MATRIX STATUS: Welcome to the construct")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.")
    print()
    print("Package installation path:")
    print(f"  {package_path}")


def main() -> None:
    """Detect virtual environment and display status."""
    venv_path: str | None = sys.prefix \
        if sys.prefix != sys.base_prefix else None

    if venv_path is None:
        show_outside_matrix()
    else:
        show_inside_construct(venv_path)


if __name__ == "__main__":
    main()
