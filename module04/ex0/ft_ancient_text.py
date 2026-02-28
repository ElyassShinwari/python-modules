def recover_ancient_text() -> None:
    """Recover data from the ancient fragment storage vault."""
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        file = open("ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("Error: Storage vault not found. Run data genrator first.")
        return
    content = file.read()
    file.close
    print("Connection established...\n")
    print("RECOVERED DATA:")
    lines = content.strip().split("\n")
    fragment_num = 1
    for line in lines:
        if line.strip():
            print(f"{line.strip()}")
            fragment_num = fragment_num + 1
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    recover_ancient_text()
