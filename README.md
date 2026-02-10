# TOPSIS-Based Evaluation of Conversational AI Models

This project applies the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method to rank pre-trained conversational AI models based on multiple evaluation criteria.

---

## Dataset Details

**Input File**

data/conversational_models.csv

**Columns**

- `Model`
- `Accuracy`
- `Speed_Score`
- `Memory_Usage`
- `Human_Score`

---

## Methodology

The TOPSIS method is implemented using the following steps:

1. Normalization of the decision matrix  
2. Assignment of weights to criteria  
3. Identification of ideal best and ideal worst solutions  
4. Calculation of distance from ideal solutions  
5. Computation of TOPSIS score  
6. Ranking of conversational models  

**Weights Used**

- Accuracy: 0.30  
- Speed Score: 0.25  
- Memory Usage: 0.20  
- Human Score: 0.25  

Memory usage is treated as a **cost criterion**.

---

## Results

| Rank | Model | TOPSIS Score |
|------|-------|--------------|
| 1 | DialoGPT | 0.824146 |
| 2 | GPT-2 | 0.773105 |
| 3 | Godel | 0.708741 |
| 4 | Blenderbot | 0.563114 |
| 5 | LLaMA-2 | 0.226895 |

The complete ranking results are saved in:

results/rankings.csv

---

## Visualization

The following bar chart shows the TOPSIS scores of all conversational models.  
A higher score indicates a better-performing model.

<p align="center">
  <img src="results/graphs.png" alt="TOPSIS Scores" width="750">
</p>
