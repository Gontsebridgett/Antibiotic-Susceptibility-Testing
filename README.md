# Antibiotic Susceptibility Testing (Kirby-Bauer Disk Diffusion)

A protocol for determining bacterial susceptibility to antibiotics using the
disk diffusion method, paired with a Python script that measures zone-of-
inhibition diameters and classifies each isolate as Susceptible, Intermediate,
or Resistant against CLSI-style breakpoint tables.

## Overview

The Kirby-Bauer disk diffusion method assesses how effectively an antibiotic
inhibits bacterial growth. A bacterial lawn is spread on Mueller-Hinton agar,
antibiotic-impregnated disks are placed on the surface, and the antibiotic
diffuses outward creating a concentration gradient. After incubation, a clear
zone (no bacterial growth) forms around effective disks. The diameter of this
zone of inhibition is measured and compared against standardised breakpoint
tables to classify the isolate's susceptibility.

## Principle

- Antibiotic diffuses radially from the disk, creating a decreasing concentration gradient
- Zone diameter is inversely related to the minimum inhibitory concentration (MIC)
- Larger zone = more susceptible organism; smaller/no zone = more resistant organism
- Each antibiotic has its own breakpoint table (zone diameters defining
  Susceptible / Intermediate / Resistant), since potency and diffusion rates differ

## Materials & Reagents

- Mueller-Hinton agar plates
- Pure bacterial isolate, standardised to 0.5 McFarland turbidity
- Sterile cotton swabs
- Antibiotic disks (e.g. Ampicillin, Ciprofloxacin, Gentamicin, Tetracycline)
- Sterile forceps, disk dispenser (optional)
- Incubator (35&ndash;37&deg;C)
- Calipers or ruler for zone measurement

## Method (Summary)

| Step | Action |
|---|---|
| 1 | Standardise bacterial suspension to 0.5 McFarland turbidity |
| 2 | Swab suspension evenly across Mueller-Hinton agar surface (lawn inoculation) |
| 3 | Place antibiotic disks on the agar surface, spaced adequately apart |
| 4 | Incubate at 35&ndash;37&deg;C for 16&ndash;18 hours |
| 5 | Measure the diameter of each zone of inhibition (mm) |
| 6 | Compare measured zones against breakpoint tables to classify susceptibility |

## Result Interpretation

Each antibiotic has its own breakpoints; example ranges (illustrative, not for
clinical use):

| Antibiotic | Resistant (mm) | Intermediate (mm) | Susceptible (mm) |
|---|---|---|---|
| Ampicillin | &le;13 | 14&ndash;16 | &ge;17 |
| Ciprofloxacin | &le;15 | 16&ndash;20 | &ge;21 |
| Gentamicin | &le;12 | 13&ndash;14 | &ge;15 |
| Tetracycline | &le;14 | 15&ndash;18 | &ge;19 |

## Analysis Script

`ast_analysis.py` reads measured zone diameters per isolate/antibiotic
combination from `sample_data/zone_measurements.csv`, applies the breakpoint
table, and classifies each result as Susceptible, Intermediate, or Resistant.

### Usage

```bash
pip install -r requirements.txt
python ast_analysis.py
```

### Sample output

```
Isolate      Antibiotic       Zone(mm)   Classification
---------------------------------------------------------
Isolate_1    Ampicillin       8          Resistant
Isolate_1    Ciprofloxacin    24         Susceptible
Isolate_1    Gentamicin       16         Susceptible
Isolate_2    Ampicillin       19         Susceptible
Isolate_2    Ciprofloxacin    14         Resistant
```

## Repository Structure

```
antibiotic-susceptibility-testing/
├── README.md
├── ast_analysis.py
├── requirements.txt
└── sample_data/
    └── zone_measurements.csv
```

## Disclaimer

Breakpoint values here are illustrative examples for educational purposes,
not sourced from a current CLSI/EUCAST table. Real clinical interpretation
must use the current official breakpoint tables for the specific organism
and antibiotic.
