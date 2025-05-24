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