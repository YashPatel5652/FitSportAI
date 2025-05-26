import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
import numpy as np
import plotly.express as px

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("PATH_OF_YOUR_FIREBASE_ADMIN_JASON_FILE")
    firebase_admin.initialize_app(cred)
db = firestore.client()

if "user_id" not in st.session_state:
    st.warning("⚠️ You must log in to access this page.")
    st.stop()

st.title("Workout History & Progress Analysis")
user_id = st.session_state["user_id"]
workouts_ref = db.collection("users").document(user_id).collection("workouts").stream()

data = []
for workout in workouts_ref:
    record = workout.to_dict()
    data.append([record["timestamp"].strftime('%Y-%m-%d'), record["exercise"], record["reps"], record["calories"], record["goal_calories"]])

if data:
    df = pd.DataFrame(data, columns=["Date", "Exercise", "Reps", "Calories Burned", "Goal Calories"])
    
    st.write("### Workout Data")
    st.dataframe(df)
    
    # Summary Statistics
    st.write("### Workout Summary")
    st.write(f"Total Workouts: {len(df)}")
    st.write(f"Total Calories Burned: {df['Calories Burned'].sum():.2f} kcal")
    
    # Visualization
    st.write("### Calories Burned vs Goal")
    fig = px.bar(df, x="Date", y=["Calories Burned", "Goal Calories"], barmode='group', title="Calories Burned vs Goal Over Time")
    st.plotly_chart(fig)
    
    st.write("### Reps Per Exercise")
    fig2 = px.pie(df, names="Exercise", values="Reps", title="Exercise Distribution")
    st.plotly_chart(fig2)
else:
    st.write("No past workout data available.")
