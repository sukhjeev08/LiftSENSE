import streamlit as st
import pandas as pd
import joblib

from recommendation_logic import get_workout_focus, get_calorie_goal

# Loding the model
def load_model():
    return joblib.load("fat_percentage_pipeline.pkl")


model = load_model()


# Designing the UI
st.set_page_config(
    page_title="LiftSENSE",
    layout="centered"
)


st.markdown(
    """
    <style>
    .stApp {
        background-color: #2f2f2f;
    }

    .header-box {
        background-color: #f5d000;
        padding: 20px 30px;
        border-radius: 18px;
        margin-bottom: 35px;
        display: flex;
        align-items: center;
    }

    .header-title {
        color: black;
        font-size: 42px;
        font-weight: 800;
        margin: 0;
    }

    .stButton > button {
        background-color: #28a745;
        color: white;
        font-size: 18px;
        padding: 10px 25px;
        border-radius: 8px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #218838;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <div class="header-box">
        <h1 class="header-title" style='color:black'>LiftSENSE</h1>
    </div>
    """,
    unsafe_allow_html=True
)


# User Inputs

# Age
st.subheader("Age")
age = st.slider(' ', 18, 80, 25)

# Height
st.subheader("Height")
col1, col2 = st.columns(2)
with col1:
    height_ft = st.number_input("Feet", min_value=3, max_value=8, value=5)
with col2:
    height_in = st.number_input("Inches", min_value=0, max_value=11, value=6)

# Weight
st.subheader("Weight")
weight = st.number_input(
    "Enter Weight in KGs",
    min_value=30.0,
    max_value=200.0,
    value=65.0,
    step=0.5,
    format="%.1f"
)

# Experience
st.subheader("Experience")
experience = st.selectbox(
    "",
    ["Beginner", "Intermediate", "Advanced"]
)

# Workout days
st.subheader("Activity Level")
workout_days = st.slider("Workout days per week", 0, 7, 3)

# Sex
st.subheader("Sex")
gender = st.radio(
    " ",
    ["Male", "Female"],
    horizontal=True
)

# Prediction Logic

if st.button("Predict"):
    total_inches = height_ft * 12 + height_in
    height_m = total_inches * 0.0254

    
    bmi = weight / (height_m ** 2)

    
    experience_map = {
        "Beginner": 1,
        "Intermediate": 2,
        "Advanced": 3
    }
    experience_level = experience_map[experience]

    user_df = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Weight (kg)": weight,
        "Height (m)": height_m,
        "BMI": bmi,
        "Workout_Frequency (days/week)": workout_days,
        "Experience_Level": experience_level
    }])

    fat_pct = model.predict(user_df)[0]

    workout_focus = get_workout_focus(
        fat_pct,
        experience_level
    )

    calorie_goal = get_calorie_goal(
        fat_pct,
        workout_days,
        experience_level
    )

    st.success("Analysis Complete ✅")

    st.metric("Estimated Body Fat %", f"{fat_pct:.2f}%")

    col1, col2 = st.columns(2)
    col1.metric("Workout Focus", workout_focus)
    col2.metric("Calorie Goal", calorie_goal)



st.markdown("---")
st.caption("Website created by Sukhjeev as a part of ML learning Journey")
