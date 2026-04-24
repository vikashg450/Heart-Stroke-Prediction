# Heart Stroke Risk Prediction 🫀

This is a Machine Learning web application built using **Streamlit** that predicts the risk of a heart stroke based on various health parameters. The model uses K-Nearest Neighbors (KNN) to classify whether a person has a high or low risk of heart disease.

## Features ✨
- **Interactive User Interface**: Built with Streamlit for a seamless experience.
- **Real-time Prediction**: Instantly get your heart disease risk prediction by tweaking health metrics.
- **Comprehensive Inputs**: Takes into account critical parameters such as Age, Cholesterol, Blood Pressure, Max Heart Rate, and ECG results.

## Data Inputs 📊
The application requires the following information to make a prediction:
- **Age**: Age of the patient
- **Sex**: Male (M) or Female (F)
- **Chest Pain Type**: ATA, NAP, TA, or ASY
- **Resting Blood Pressure**: mm Hg
- **Cholesterol**: mg/dL
- **Fasting Blood Sugar**: > 120 mg/dL (1 = true; 0 = false)
- **Resting ECG**: Normal, ST, LVH
- **Max Heart Rate**: Maximum heart rate achieved
- **Exercise-Induced Angina**: Y or N
- **Oldpeak**: ST depression induced by exercise relative to rest
- **ST Slope**: Up, Flat, or Down

## Tech Stack 🛠️
- **Python**: Core programming language
- **Streamlit**: Web framework for building the UI
- **Pandas**: Data manipulation and feature engineering
- **Scikit-learn**: Machine Learning library (KNN model & Scaler)
- **Joblib**: Model serialization

## Installation 🚀

1. Clone this repository:
```bash
git clone <your-repository-url>
cd <your-repository-folder>
```

2. Install the required dependencies:
```bash
pip install streamlit pandas scikit-learn joblib
```

3. Run the Streamlit application:
```bash
python -m streamlit run app.py
```

## How It Works 🧠
1. **Input Collection**: The user inputs their health metrics via the Streamlit interface.
2. **Preprocessing**: The input data is transformed into a DataFrame, missing expected columns are padded with `0`, and then it is normalized using the pre-fitted `StandardScaler` (`heart_scaler.pkl`).
3. **Prediction**: The processed data is fed into the trained KNN model (`knn_heart_model.pkl`).
4. **Result**: The app displays whether the user has a **High Risk** or **Low Risk** of heart disease.

## Files Included 📁
- `app.py`: The main Streamlit application code.
- `knn_heart_model.pkl`: The trained K-Nearest Neighbors model.
- `heart_scaler.pkl`: The scaler used to normalize the input data.
- `heart_columns.pkl`: The expected columns generated during training (used to align new input data).
- `HeartdiseaseFinal.ipynb`: Jupyter Notebook containing data exploration, model training, and evaluation steps.

## Author 👤
Created by **Vikash kumar**.
