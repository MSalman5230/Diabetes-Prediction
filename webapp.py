import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("diabetes_model.pkl", "rb") as file:
    model = pickle.load(file)


# Function to preprocess user input
def preprocess_input(user_input):
    # Convert user input to DataFrame
    input_df = pd.DataFrame([user_input])

    # One-hot encode categorical features
    # input_df = pd.get_dummies(input_df, columns=["gender", "smoking_history"])

    return input_df


# Function to make predictions
def predict_diabetes(user_input):
    input_df = preprocess_input(user_input)
    prediction = model.predict(input_df)
    if prediction[0]:
        return ":red[You have Diabetes, Consult Doctor]"
    return ":green[No Diabetes, Hurray]"
    # return prediction[0]


# Streamlit app
def main():
    st.title("Diabetes Prediction App")

    # User input form
    st.header("Patient information")

    gender = st.radio(
        "Gender", ["Male", "Female"], help="Select the gender of the patient."
    )
    age = st.slider("Age", 1, 100, 30, help="Enter the age of the patient.")
    hypertension = st.checkbox(
        "Hypertension",
        help="Check if the patient has been diagnosed with hypertension.",
    )
    heart_disease = st.checkbox(
        "Heart Disease",
        help="Check if the patient has been diagnosed with heart disease.",
    )

    smoking_history = st.selectbox(
        "Smoking History",
        ["No Info", "never", "former", "current"],
        help="Select the smoking history of the patient.",
    )

    bmi = st.slider(
        "BMI", 10.0, 50.0, 25.0, help="Enter the Body Mass Index (BMI) of the patient."
    )
    hba1c_level = st.slider(
        "HbA1c Level",
        4.0,
        10.0,
        6.0,
        help="Enter the HbA1c level (HbA1c is your average blood glucose (sugar) levels for the last two to three months) of the patient.",
    )
    blood_glucose_level = st.slider(
        "Blood Glucose Level",
        50,
        300,
        120,
        help="Enter the blood glucose level of the patient.",
    )

    user_input = {
        "gender": gender,
        "age": age,
        "hypertension": 1 if hypertension else 0,
        "heart_disease": 1 if heart_disease else 0,
        "smoking_history": smoking_history,
        "bmi": bmi,
        "HbA1c_level": hba1c_level,
        "blood_glucose_level": blood_glucose_level,
    }

    # Button to trigger prediction
    if st.button("Predict Diabetes"):
        # Make prediction
        prediction = predict_diabetes(user_input)

        # Display prediction result
        st.subheader("Prediction Result")
        st.write("Diabetes Prediction:", prediction)

    st.markdown(
        "[Project Source Code](https://github.com/MSalman5230/Diabetes-Prediction)"
    )


if __name__ == "__main__":
    main()
