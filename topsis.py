import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# Data
data = {
    "Model": ["DialoGPT", "Blenderbot", "Godel", "GPT-2", "LLaMA-2"],
    "Accuracy": [0.82, 0.92, 0.88, 0.75, 0.95],
    "Speed_Score": [0.9, 0.5, 0.7, 0.95, 0.3],
    "Memory_Usage": [450, 1100, 850, 350, 2500],
    "Human_Score": [7, 9, 8, 6, 9]
}
df = pd.DataFrame(data)

# Output dirs
root = Path(__file__).resolve().parent.parent
data_dir = root / "data"
results_dir = root / "results"
data_dir.mkdir(parents=True, exist_ok=True)
results_dir.mkdir(parents=True, exist_ok=True)

# Save input CSV
input_csv = data_dir / "conversational_models.csv"
df.to_csv(input_csv, index=False)

# Normalize
matrix = df.iloc[:, 1:].values
norm_matrix = matrix / np.sqrt((matrix**2).sum(axis=0))

# Weights
weights = np.array([0.3, 0.25, 0.2, 0.25])

# Criteria (+1 benefit, -1 cost)
criteria = np.array([1, 1, -1, 1])

# Weighted normalized matrix
weighted_matrix = norm_matrix * weights * criteria

# Ideal best/worst
ideal_best = np.max(weighted_matrix, axis=0)
ideal_worst = np.min(weighted_matrix, axis=0)

# Distances to ideals
dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

# TOPSIS score
score = dist_worst / (dist_best + dist_worst)

# Add score and rank
df["TOPSIS_Score"] = score
# Rank (1 = best)
df["Rank"] = df["TOPSIS_Score"].rank(ascending=False, method="dense").astype(int)

# Save rankings
rankings_csv = results_dir / "rankings.csv"
df.to_csv(rankings_csv, index=False)

# Print results
print("\nFinal Results with TOPSIS Ranking:")
print(df)

# Save plot
plt.figure(figsize=(8, 5))
plt.bar(df["Model"], df["TOPSIS_Score"], color="skyblue")
plt.xlabel("Models")
plt.ylabel("TOPSIS Score")
plt.title("TOPSIS Ranking of Conversational Models")
plot_path = results_dir / "graphs.png"
plt.savefig(plot_path, bbox_inches="tight")
plt.close()

print(f"Saved input data to: {input_csv}")
print(f"Saved rankings to: {rankings_csv}")
print(f"Saved plot to: {plot_path}")