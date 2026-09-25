"""
ast_analysis.py

Classifies bacterial isolate antibiotic susceptibility (Susceptible /
Intermediate / Resistant) from measured Kirby-Bauer disk diffusion zone
diameters, using illustrative breakpoint tables.
"""

import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "sample_data" / "zone_measurements.csv"

# Illustrative breakpoints (mm): (resistant_max, intermediate_max)
# zone <= resistant_max -> Resistant
# resistant_max < zone <= intermediate_max -> Intermediate
# zone > intermediate_max -> Susceptible
BREAKPOINTS = {
    "Ampicillin": (13, 16),
    "Ciprofloxacin": (15, 20),
    "Gentamicin": (12, 14),
    "Tetracycline": (14, 18),
}


def classify(antibiotic: str, zone_mm: int) -> str:
    if antibiotic not in BREAKPOINTS:
        return "Unknown antibiotic — no breakpoint data"
    resistant_max, intermediate_max = BREAKPOINTS[antibiotic]
    if zone_mm <= resistant_max:
        return "Resistant"
    elif zone_mm <= intermediate_max:
        return "Intermediate"
    return "Susceptible"


def load_data(path: Path):
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["zone_mm"] = int(row["zone_mm"])
    return rows


def main():
    rows = load_data(DATA_PATH)

    print(f"{'Isolate':<13}{'Antibiotic':<17}{'Zone(mm)':<11}{'Classification'}")
    print("-" * 59)
    for row in rows:
        result = classify(row["antibiotic"], row["zone_mm"])
        print(f"{row['isolate_id']:<13}{row['antibiotic']:<17}{row['zone_mm']:<11}{result}")

    resistant_count = sum(1 for r in rows if classify(r["antibiotic"], r["zone_mm"]) == "Resistant")
    print(f"\n{resistant_count} of {len(rows)} isolate-antibiotic combinations classified as Resistant.")


if __name__ == "__main__":
    main()
