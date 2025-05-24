import pandas as pd

# Load your datasets
attributes_df = pd.read_csv(r"C:\Users\trusk\Downloads\Patient_Attributes - Patient_Attributes (2).csv")
admissions_df = pd.read_csv(r"C:\Users\trusk\Downloads\Patient_Admissions - Patient_Admissions (2).csv")

# --- Clean column names for consistency ---
admissions_df.columns = [col.strip().replace(" ", "_") for col in admissions_df.columns]
attributes_df.columns = [col.strip().replace(" ", "_") for col in attributes_df.columns]

# --- Ensure MLR is numeric ---
attributes_df['MLR'] = pd.to_numeric(attributes_df['MLR'], errors='coerce')

# --- Merge admissions with patient attributes ---
merged_df = admissions_df.merge(attributes_df, left_on='Patient_ID', right_on='PatientID', how='left')

# --- Count hospitalizations per cohort ---
hospitalization_counts = merged_df.groupby('Cohort')['Admission_ID'].nunique()

# --- Cost assumptions ---
hospitalization_cost = 16000
hospitalization_costs = hospitalization_counts * hospitalization_cost

# --- Calculate average MLR per cohort ---
avg_mlr = attributes_df.groupby('Cohort')['MLR'].mean()

# --- Count patients in each cohort ---
patient_counts = attributes_df['Cohort'].value_counts()

# --- Create summary table ---
summary_df = pd.DataFrame({
    'Total Patients': patient_counts,
    'Hospitalizations': hospitalization_counts,
    'Hospitalization Cost': hospitalization_costs,
    'Average MLR': avg_mlr
})

# --- Display result ---
print(summary_df)


import matplotlib.pyplot as plt

# Data for the visuals
hospitalizations = [555, 223]  # Control, Treatment
costs = [8880000, 3568000]     # Hospitalization costs
mlrs = [0.905, 0.654]          # Average MLRs
groups = ['Control', 'Treatment']

# --- Plot 1: Hospitalizations ---
plt.figure(figsize=(6, 4))
plt.bar(groups, hospitalizations, color=["gray", "green"])
plt.title("Total Hospitalizations by Cohort")
plt.ylabel("Number of Hospitalizations")
plt.tight_layout()
plt.savefig("hospitalizations_by_cohort.png")
plt.close()

# --- Plot 2: Hospitalization Cost ---
plt.figure(figsize=(6, 4))
plt.bar(groups, [c / 1e6 for c in costs], color=["gray", "green"])
plt.title("Hospitalization Cost by Cohort (in Millions $)")
plt.ylabel("Cost (Millions $)")
plt.tight_layout()
plt.savefig("hospitalization_cost_by_cohort.png")
plt.close()

# --- Plot 3: MLR Comparison ---
plt.figure(figsize=(6, 4))
plt.bar(groups, mlrs, color=["gray", "green"])
plt.title("Average MLR by Cohort")
plt.ylabel("MLR (Medical Loss Ratio)")
plt.axhline(1, color='red', linestyle='--', label='Breakeven (MLR=1)')
plt.legend()
plt.tight_layout()
plt.savefig("mlr_by_cohort.png")
plt.close()