# TOPSIS Conversational Models — Results

## Overview
This project ranks conversational models using the TOPSIS multi-criteria decision-making method and saves results and visualizations in the `results/` folder.

## Dataset
- Input file: data/conversational_models.csv
- Columns: `Model`, `Accuracy`, `Speed_Score`, `Memory_Usage`, `Human_Score`

## Method
- Normalize criteria, apply weights, compute ideal best/worst, and calculate TOPSIS scores and ranks.
- Weights used: Accuracy 0.3, Speed 0.25, Memory 0.2, Human 0.25
- Memory_Usage is treated as a cost criterion.

## Results (TOPSIS Scores)
| Rank | Model     | TOPSIS Score |
|------|-----------|--------------|
| 1    | DialoGPT  | 0.824146     |
| 2    | GPT-2     | 0.773105     |
| 3    | Godel     | 0.708741     |
| 4    | Blenderbot| 0.563114     |
| 5    | LLaMA-2   | 0.226895     |

Full CSV of results: [results/rankings.csv](results/rankings.csv)

## Visualization
Bar chart of TOPSIS scores:

![TOPSIS Scores](results/graphs.png)

## How to reproduce
1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1    # or use .venv\Scripts\python directly
pip install -r requirements.txt
```

2. Run the script:

```powershell
.venv\Scripts\python code\topsis.py
```

Outputs will be written to:
- [data/conversational_models.csv](data/conversational_models.csv)
- [results/rankings.csv](results/rankings.csv)
- [results/graphs.png](results/graphs.png)

If you want this file saved as `README.md`, please remove or rename the existing `README.md` directory at the project root and I will create `README.md` in its place.
