"""Loading Programs - Data analysis with dependency management."""

import sys
import importlib


REQUIRED_PACKAGES: dict[str, str] = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}


def check_package(name: str) -> tuple[bool, str]:
    """Check if a package is installed and return its version."""
    try:
        module = importlib.import_module(name)
        version: str = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, ""


def check_dependencies() -> bool:
    """Check all required dependencies and display status."""
    print("Checking dependencies:")
    all_ok: bool = True
    for name, description in REQUIRED_PACKAGES.items():
        found, version = check_package(name)
        if found:
            print(f"  [OK] {name} ({version}) - {description} ready")
        else:
            print(f"  [MISSING] {name} - {description} not available")
            all_ok = False
    return all_ok


def show_install_instructions() -> None:
    """Show installation instructions for pip and Poetry."""
    print()
    print("To install dependencies with pip:")
    print("  pip install -r requirements.txt")
    print()
    print("To install dependencies with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")
    print()
    print("pip vs Poetry:")
    print("  pip   - Simple, uses requirements.txt, no lock file")
    print("         by default, flat dependency list.")
    print("  Poetry - Uses pyproject.toml + poetry.lock,")
    print("           resolves dependency conflicts, manages")
    print("           virtual environments automatically.")


def run_analysis() -> None:
    """Run Matrix data analysis using numpy, pandas, matplotlib."""
    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    plt_module = importlib.import_module("matplotlib.pyplot")

    print()
    print("Analyzing Matrix data...")

    rng = np.random.default_rng(42)
    n_points: int = 1000

    timestamps = np.arange(n_points)
    signal_strength = rng.normal(loc=50, scale=15, size=n_points)
    anomaly_score = np.abs(rng.standard_normal(n_points)) * 10
    threat_level = (
        signal_strength * 0.3 + anomaly_score * 0.7
        + rng.uniform(-5, 5, size=n_points)
    )

    print(f"Processing {n_points} data points...")

    df = pd.DataFrame({
        "timestamp": timestamps,
        "signal_strength": signal_strength,
        "anomaly_score": anomaly_score,
        "threat_level": threat_level,
    })

    stats = df.describe()
    print()
    print("Matrix Data Summary:")
    print(f"  Mean signal strength: {stats['signal_strength']['mean']:.2f}")
    print(f"  Mean anomaly score:   {stats['anomaly_score']['mean']:.2f}")
    print(f"  Mean threat level:    {stats['threat_level']['mean']:.2f}")

    print()
    print("Generating visualization...")

    fig, axes = plt_module.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Matrix Data Analysis", fontsize=14)

    axes[0][0].plot(df["timestamp"], df["signal_strength"],
                    linewidth=0.5, color="green")
    axes[0][0].set_title("Signal Strength Over Time")
    axes[0][0].set_xlabel("Timestamp")
    axes[0][0].set_ylabel("Signal")

    axes[0][1].hist(df["anomaly_score"], bins=30, color="red",
                    alpha=0.7)
    axes[0][1].set_title("Anomaly Score Distribution")
    axes[0][1].set_xlabel("Score")
    axes[0][1].set_ylabel("Frequency")

    axes[1][0].scatter(df["signal_strength"], df["threat_level"],
                       alpha=0.3, s=5, color="cyan")
    axes[1][0].set_title("Signal vs Threat Level")
    axes[1][0].set_xlabel("Signal Strength")
    axes[1][0].set_ylabel("Threat Level")

    rolling_mean = df["threat_level"].rolling(window=50).mean()
    axes[1][1].plot(df["timestamp"], df["threat_level"],
                    alpha=0.3, linewidth=0.5, label="Raw")
    axes[1][1].plot(df["timestamp"], rolling_mean,
                    color="yellow", linewidth=1.5,
                    label="Rolling Mean")
    axes[1][1].set_title("Threat Level Trend")
    axes[1][1].set_xlabel("Timestamp")
    axes[1][1].set_ylabel("Threat Level")
    axes[1][1].legend()
    plt_module.show()

    plt_module.tight_layout()
    output_file: str = "matrix_analysis.png"
    plt_module.savefig(output_file, dpi=150)
    plt_module.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_file}")


def show_version_comparison() -> None:
    """Show installed package versions comparison."""
    print()
    print("Package version comparison:")
    for name in REQUIRED_PACKAGES:
        found, version = check_package(name)
        if found:
            print(f"  {name:15s} {version}")


def main() -> None:
    """Main entry point for the loading program."""
    print("LOADING STATUS: Loading programs...")
    print()

    all_ok: bool = check_dependencies()

    if not all_ok:
        print()
        print("ERROR: Some dependencies are missing!")
        show_install_instructions()
        sys.exit(1)

    show_version_comparison()
    run_analysis()


if __name__ == "__main__":
    main()