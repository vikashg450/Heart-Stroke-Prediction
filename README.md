# 🫀 Heart Stroke Risk Prediction

> A machine learning web application that predicts cardiovascular disease risk using K-Nearest Neighbors (KNN) — built with Streamlit for real-time, interactive health assessments.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://heart-stroke-prediction-dertr7onttaxf8qp8wbgsb.streamlit.app/)
---

## 📸 Preview

<!-- Add a screenshot of your app here -->
<img width="1864" height="830" alt="image" src="https://github.com/user-attachments/assets/de3c9c8d-c4fa-42c5-87c0-a0e0402b15d3" />


---

## ✨ Features

- **Real-time Prediction** — Instantly get a High Risk or Low Risk classification by adjusting health parameters
- **Interactive UI** — Clean, responsive interface built entirely with Streamlit
- **11 Health Inputs** — Covers age, cholesterol, blood pressure, ECG, heart rate, and more
- **Normalized Inference** — Pre-fitted `StandardScaler` ensures consistent predictions on new inputs
- **Trained KNN Model** — Serialized model for fast, offline-capable inference

---

## 📊 Health Parameters

| Parameter | Description | Type |
|-----------|-------------|------|
| Age | Patient age | Numeric |
| Sex | Male (M) / Female (F) | Categorical |
| Chest Pain Type | ATA, NAP, TA, ASY | Categorical |
| Resting BP | Resting blood pressure (mm Hg) | Numeric |
| Cholesterol | Serum cholesterol (mg/dL) | Numeric |
| Fasting Blood Sugar | > 120 mg/dL (1 = Yes, 0 = No) | Binary |
| Resting ECG | Normal, ST, LVH | Categorical |
| Max Heart Rate | Maximum heart rate achieved | Numeric |
| Exercise Angina | Exercise-induced angina (Y/N) | Binary |
| Oldpeak | ST depression (exercise vs. rest) | Numeric |
| ST Slope | Up, Flat, Down | Categorical |

---

## 🧠 How It Works

```
User Input  →  DataFrame  →  Align Columns  →  StandardScaler  →  KNN Model  →  Result
```

1. **Input Collection** — User fills health metrics via the Streamlit UI
2. **Preprocessing** — Input is structured into a DataFrame; missing expected columns are padded with `0`
3. **Normalization** — Data is scaled using the pre-fitted `heart_scaler.pkl`
4. **Prediction** — Scaled input is passed to `knn_heart_model.pkl`
5. **Output** — App returns **🔴 High Risk** or **🟢 Low Risk**

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| Python 3.8+ | Core language |
| Streamlit | Web UI framework |
| Scikit-learn | KNN model & StandardScaler |
| Pandas | Data manipulation |
| Joblib | Model serialization |

---

## 📁 Project Structure

```
heart-stroke-predictor/
│
├── app.py                    # Main Streamlit application
├── knn_heart_model.pkl       # Trained KNN classifier
├── heart_scaler.pkl          # Pre-fitted StandardScaler
├── heart_columns.pkl         # Expected feature columns
├── HeartdiseaseFinal.ipynb   # EDA, training & evaluation notebook
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/heart-stroke-predictor.git
cd heart-stroke-predictor
```

### 2. Install dependencies

```bash
pip install streamlit pandas scikit-learn joblib
```

### 3. Run the app

```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.


---

## 📓 Notebook

The `HeartdiseaseFinal.ipynb` notebook covers:
- Exploratory Data Analysis (EDA)
- Feature engineering & encoding
- Model training and hyperparameter tuning
- Evaluation metrics (accuracy, confusion matrix, classification report)
- Exporting the model and scaler with Joblib

---

## ⚠️ Disclaimer

This application is intended for **educational and research purposes only**. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider for medical decisions.

---

## 👤 Author

**Vikash Kumar**
