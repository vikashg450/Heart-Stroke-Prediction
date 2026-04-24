import streamlit as st
import pandas as pd
import joblib

# Set page configuration for a professional look
st.set_page_config(
    page_title="HeartGuard AI",
    page_icon="❤️",
    layout="wide"
)

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff3333;
        border: none;
    }
    .reportview-container .main .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Load saved model assets
@st.cache_resource
def load_assets():
    model = joblib.load("knn_heart_model.pkl")
    scaler = joblib.load("heart_scaler.pkl")
    expected_columns = joblib.load("heart_columns.pkl")
    return model, scaler, expected_columns

try:
    model, scaler, expected_columns = load_assets()
except Exception as e:
    st.error("Error loading model files. Please ensure .pkl files are in the directory.")

# --- SIDEBAR / BRANDING ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/822/822118.png", width=100)
    st.title("HeartGuard AI")
    st.info("This tool uses Machine Learning (KNN) to assess the probability of heart-related complications.")
    st.markdown("---")
    st.caption("Developed by Vikash")

# --- MAIN UI ---
st.title("❤️ Heart Disease Risk Assessment")
st.write("Complete the clinical profile below to generate a risk report.")

# Organizing inputs into columns (Cards)
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📋 Patient Profile")
    age = st.number_input("Age", 18, 100, 40)
    sex = st.radio("Sex", ["M", "F"], horizontal=True)
    resting_bp = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)

with col2:
    st.subheader("🧪 Clinical Tests")
    cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
    resting_ecg = st.selectbox("Resting ECG Result", ["Normal", "ST", "LVH"])
    max_hr = st.slider("Max Heart Rate Achieved", 60, 220, 150)

with col3:
    st.subheader("🏃 Physical Activity")
    chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
    exercise_angina = st.radio("Exercise-Induced Angina", ["Y", "N"], horizontal=True)
    oldpeak = st.slider("ST Depression (Oldpeak)", 0.0, 6.0, 1.0)
    st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

st.markdown("---")

# --- PREDICTION LOGIC ---
if st.button("GENERATE RISK ANALYSIS"):
    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Data Processing
    input_df = pd.DataFrame([raw_input])
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0
    
    input_df = input_df[expected_columns]
    scaled_input = scaler.transform(input_df)
    
    # Prediction
    prediction = model.predict(scaled_input)[0]
    # Get probability if model supports it
    try:
        prob = model.predict_proba(scaled_input)[0][1] * 100
    except:
        prob = None

    # --- RESULTS DISPLAY ---
    st.subheader("📊 Analysis Result")
    
    res_col1, res_col2 = st.columns([1, 2])
    
    with res_col1:
        if prediction == 1:
            st.error("### HIGH RISK")
            st.metric(label="Risk Status", value="Positive", delta="Alert", delta_color="inverse")
        else:
            st.success("### LOW RISK")
            st.metric(label="Risk Status", value="Negative", delta="Clear")

    with res_col2:
        if prediction == 1:
            st.warning("**Recommendation:** Based on the input parameters, we recommend consulting a cardiologist for a comprehensive check-up.")
        else:
            st.info("**Health Tip:** Your results look good! Maintain a balanced diet and regular exercise to keep your heart healthy.")
            
        if prob is not None:
            st.write(f"Confidence Level: **{prob:.2f}%**")
            st.progress(prob / 100)