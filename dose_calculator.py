# Pharma Dose Calculator v2 (learning project, not for clinical use)

drugs = {
    "paracetamol": {"mg_per_kg": 15, "max_dose_mg": 1000},
    "ibuprofen": {"mg_per_kg": 10, "max_dose_mg": 400},
    "amoxicillin": {"mg_per_kg": 25, "max_dose_mg": 500},
}

def calculate_dose(drug_name, weight_kg):
    info = drugs[drug_name]
    dose = info["mg_per_kg"] * weight_kg
    capped = dose > info["max_dose_mg"]
    if capped:
        dose = info["max_dose_mg"]
    return dose, capped

print("=== Pharma Dose Calculator v2 ===")
print("Available drugs:", ", ".join(drugs.keys()))

name = input("Patient name: ")
weight = float(input("Weight (kg): "))
drug = input("Drug name: ").strip().lower()

if drug not in drugs:
    print("Drug not in list. Please add it to the drugs dictionary.")
else:
    dose, capped = calculate_dose(drug, weight)
    print(f"\nPatient: {name} | Weight: {weight} kg")
    print(f"Drug: {drug.title()}")
    print(f"Calculated single dose: {dose:.0f} mg")
    if capped:
        print("WARNING: Calculated dose exceeded the maximum, so it was limited to the max single dose.")
    print("Note: example values only. Always confirm with a doctor or pharmacist.")
