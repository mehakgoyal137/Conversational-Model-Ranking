# TOPSIS-Based Evaluation of Conversational AI Models

This project applies the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method to evaluate and rank pre-trained conversational AI models using multiple performance criteria.

The objective is to identify the best conversational model based on quantitative and qualitative metrics.

---

## Dataset Details

**Input File**

data/conversational_models.csv

**Columns**

- `Model` – Name of the conversational model  
- `Accuracy` – Response accuracy score  
- `Speed_Score` – Inference speed score  
- `Memory_Usage` – Memory consumption (lower is better)  
- `Human_Score` – Human-likeness rating  

---

## Methodology

The TOPSIS method is applied using the following steps:

1. Construction of the decision matrix  
2. Normalization of criteria values  
3. Weight assignment to each criterion  
4. Identification of ideal best and ideal worst solutions  
5. Distance calculation from ideal solutions  
6. Computation of TOPSIS scores  
7. Final ranking of models  

**Weights Used**

- Accuracy: 0.30  
- Speed Score: 0.25  
- Memory Usage: 0.20  
- Human Score: 0.25  

*Memory Usage is treated as a cost criterion.*

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
  <img src="results/graphs.png" alt="TOPSIS Scores" width="700">
</p>

---

## How to Run

1. Install dependencies:

```powershell
pip install -r requirements.txt

