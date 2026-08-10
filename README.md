# Emerging-Tech-2026-Machine-Learning

A specialised model of AI focused on designing algorithms that autonomously learn,
discover statistical patterns, and improve their functional operation through experience
and data exposure without human interventions 

* Linear regression
* Model Training
* benign code

---
# Machine Learning Fundamentals & Pipeline Security

This repository demonstrates the core operational mechanics of Supervised Machine Learning using Linear Regression and outlines theoretical security considerations within the AI supply chain.

---

## Machine Learning Explanation

### 1. Training Phase (`model.fit`)
* **Features (X) & Targets (y):** The algorithm takes structured numerical inputs (X) and known outputs (y).
* **Pattern Recognition:** Instead of explicitly programming rules, the algorithm calculates optimal parameters (weights and bias) to fit a mathematical line (y = mx + c) to the training data.

### 2. Inference Phase (`model.predict`)
* Once trained, the model uses its learned weights to evaluate new, unseen feature inputs (X = 6) and predict an expected target value.

---

## Theoretical Concept: AI Supply Chain Security

In modern software development, machine learning pipelines rely heavily on third-party models, pre-trained weights, and external datasets (the AI Supply Chain).

* **Model Serialization Risks:** Machine learning models are often saved as binary files (e.g., `.pkl` via `pickle`). Unpickling models from untrusted sources can lead to arbitrary code execution because the serialization format can execute code upon loading.
* **Supply Chain Mitigation:** 
  * Always use safer, non-executable model formats (such as `Safetensors` or `ONNX`) for weight distribution.
  * Verify cryptographic hashes (e.g., SHA-256) of datasets and pre-trained weights before loading them into a production pipeline.

---

## How to Set Up and Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Mivuyo1/Emerging-Tech-2026-Machine-Learning.git]([https://github.com/Mivuyo1/ML-Demonstration.git](https://github.com/Mivuyo1/Emerging-Tech-2026-Machine-Learning.git)
   cd Emerging-Tech-2026-Machine-Learning
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Run Main.py**
   ```bash
   python main.py

   
