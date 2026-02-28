def create_arcive() -> None:
    """Create a new archive with preservation data."""
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print("Initializing new storage unit: new_discovery.txt")
    file = open("new_discovery.txt", "w")
    print("Storage unit created successfuly...\n")
    print("Inscribing perservation data...")
    entries = [
        "New quantum algorithm discovered",
        "Efficiency increased by 347%",
        "Archived by Data Archivist trainee",
    ]
    for i, entry in enumerate(entries, 1):
        file.write(f"{entry}\n")
        print((f"[ENTRY {i:03d}] {entry}"))
    file.close()
    print("\nData inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")


if __name__ == "__main__":
    create_arcive()
