import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# App title
st.title("Abuzzz!!!🧠 Depression Detection App")
st.write("Answer the following questions to check your mental wellness.")

# User Inputs
sleep_hours = st.slider('How many hours do you sleep daily?', 0, 12, 7)
sadness_level = st.slider('How often do you feel sad? (1 = Rarely, 10 = Always)', 1, 10, 5)
social_activity = st.slider('How active are you socially? (1 = Not at all, 10 = Very active)', 1, 10, 5)
energy_level = st.slider('Your daily energy level? (1 = Very low, 10 = Very high)', 1, 10, 5)

# Predict button
if st.button('Check My Mental Health'):
    input_data = np.array([[sleep_hours, sadness_level, social_activity, energy_level]])
    prediction = model.predict(input_data)
    
    # Get probability if available
    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_data)[0][1]  # Probability of class '1' (depressed)
        depression_percentage = round(prob * 100, 2)
    else:
        depression_percentage = "N/A"

    if prediction[0] == 1:
        st.error("⚠️ You might be experiencing symptoms of Depression.")
        st.subheader("💡 Some Suggestions:")
        st.write("- Talk to someone you trust.")
        st.write("- Practice mindfulness or meditation.")
        st.write("- Consult a mental health professional if symptoms persist.")
    else:
        st.success("✅ You seem to be doing well! Keep maintaining a healthy lifestyle.")

    st.markdown(f"### 🧮 Depression Likelihood: `{depression_percentage}%`")

# Footer
st.write("___")
st.write("Made by Mohammed Abu Baker")
st.caption("This tool is for initial awareness only. Not a medical diagnosis.")
