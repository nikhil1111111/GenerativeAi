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
























# import streamlit as st

# st.title("Common Diseases Prescription")

# # Define options for communicable and non-communicable diseases
# communicable_diseases = {
#     'Malaria': {
#         'advice': "Use mosquito nets while sleeping, use insect repellents, and take prescribed antimalarial medications if traveling to endemic areas.",
#         'link': "https://www.who.int/news-room/fact-sheets/detail/malaria"
#     },
#     'Tuberculosis (TB)': {
#         'advice': "Take all prescribed medications consistently, cover your mouth when coughing, and avoid close contact with others until cleared by a healthcare provider.",
#         'link': "https://www.who.int/news-room/fact-sheets/detail/tuberculosis"
#     },
#     'Dengue fever': {
#         'advice': "Use mosquito repellents, eliminate mosquito breeding sites (stagnant water), and seek medical care if you develop severe symptoms such as persistent vomiting or bleeding.",
#         'link': "https://www.who.int/news-room/fact-sheets/detail/dengue-and-severe-dengue"
#     },
#     'Typhoid': {
#         'advice': "Practice good hygiene, drink clean water, and get vaccinated if traveling to endemic areas.",
#         'link': "https://www.who.int/news-room/fact-sheets/detail/typhoid"
#     },
#     'Other vector-borne diseases': {
#         'advice': "Prevent mosquito bites and follow specific guidelines for the particular disease (e.g., Zika virus, Chikungunya).",
#         'link': "https://www.cdc.gov/vectors/index.html"
#     }
# }

# non_communicable_diseases = {
#     'Heart disease': {
#         'advice': "Maintain a healthy diet, exercise regularly, quit smoking, manage stress, and monitor cholesterol and blood pressure levels.",
#         'link': "https://www.heart.org/en/health-topics"
#     },
#     'Stroke': {
#         'advice': "Control blood pressure, manage diabetes, quit smoking, exercise regularly, and recognize stroke symptoms for immediate medical attention.",
#         'link': "https://www.stroke.org/"
#     },
#     'Cancer': {
#         'advice': "Get regular screenings, maintain a healthy weight, avoid tobacco and excessive alcohol consumption, and protect yourself from UV radiation.",
#         'link': "https://www.cancer.gov/"
#     },
#     'Chronic respiratory diseases': {
#         'advice': "Avoid smoking and secondhand smoke, manage allergies, take prescribed medications as directed, and avoid exposure to air pollutants.",
#         'link': "https://www.lung.org/lung-health-diseases"
#     },
#     'Diabetes': {
#         'advice': "Monitor blood sugar levels, maintain a healthy diet, exercise regularly, take medications as prescribed, and attend regular check-ups.",
#         'link': "https://www.diabetes.org/"
#     },
#     'Kidney diseases': {
#         'advice': "Manage blood pressure, control diabetes, avoid excessive use of pain medications, maintain a healthy weight, and stay hydrated.",
#         'link': "https://www.kidney.org/"
#     },
#     'Liver diseases': {
#         'advice': "Limit alcohol consumption, get vaccinated against hepatitis, maintain a healthy weight, and avoid risky behaviors.",
#         'link': "https://www.liverfoundation.org/"
#     },
#     'HIV/AIDS': {
#         'advice': "Use protection during sexual activity, get tested regularly, take antiretroviral medications as prescribed, and avoid sharing needles.",
#         'link': "https://www.hiv.gov/"
#     }
# }

# # Add a selectbox in the sidebar for disease selection
# selected_category = st.sidebar.selectbox("Select a category", ('Communicable diseases', 'Non-communicable diseases'))

# if selected_category == 'Communicable diseases':
#     selected_disease = st.sidebar.selectbox("Select a disease", list(communicable_diseases.keys()))
#     st.write(f"### Advice for {selected_disease}:")
#     st.write(communicable_diseases[selected_disease]['advice'])
#     st.write(f"[More information on {selected_disease}]( {communicable_diseases[selected_disease]['link']} )")

# else:
#     selected_disease = st.sidebar.selectbox("Select a disease", list(non_communicable_diseases.keys()))
#     st.write(f"### Advice for {selected_disease}:")
#     st.write(non_communicable_diseases[selected_disease]['advice'])
#     st.write(f"[More information on {selected_disease}]( {non_communicable_diseases[selected_disease]['link']} )")
