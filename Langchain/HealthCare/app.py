import streamlit as st
from langchains import run_langchain 


st.title("Health Advisor")
st.header("Age")
age = st.number_input("Enter your age", min_value=1, max_value=150, step=1)

st.header("Gender")
gender = st.radio("Select your gender", ['Male', 'Female', 'Other'])

st.header("Symptoms")
symptoms = st.text_area("Enter your symptoms (comma-separated)", height=100)

if st.button("Predict Disease and Get Prescription"):
    user_input = f"{age}, {gender}, {symptoms}"
    response = run_langchain(user_input)
    st.markdown("### Prescription:")
    st.write(response)
    st.markdown("#### Related Resources:")
    predicted_disease = response  
    
    if predicted_disease == 'Malaria':
        st.write("For more information on malaria medications and treatments, visit [CDC - Malaria Treatment](https://www.cdc.gov/malaria/diagnosis_treatment/index.html)")
    elif predicted_disease == 'Tuberculosis (TB)':
        st.write("Learn about tuberculosis treatments and medications at [WHO - Tuberculosis Treatment](https://www.who.int/tb/areas-of-work/treatment/overview/en/)")
    elif predicted_disease == 'Dengue Fever':
        st.write("Find out about dengue fever treatments and management at [Mayo Clinic - Dengue Fever](https://www.mayoclinic.org/diseases-conditions/dengue-fever/diagnosis-treatment/drc-20353085)")
    elif predicted_disease == 'Typhoid':
        st.write("Explore typhoid fever treatments and prevention strategies at [Healthline - Typhoid Fever](https://www.healthline.com/health/typhoid-fever)")
    else:
        st.write("For information specific to your disease, consult a healthcare provider or search reputable health websites.")
