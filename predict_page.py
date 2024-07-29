import streamlit as st
import pickle
import numpy as np

# Load the trained model

with open('Model/saved_steps.pkl', 'rb') as f:
    data = pickle.load(f)

reg_model=data['model']
le_country = data['le_country']
le_education=data['le_education']


def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        'United States of America',
       'United Kingdom of Great Britain and Northern Ireland',
       'Australia', 'Netherlands', 'Germany', 'Sweden', 'France', 'Spain',
       'Brazil', 'Italy', 'Canada', 'Switzerland', 'India', 'Norway',
       'Denmark', 'Israel', 'Poland'
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country=st.selectbox("Country",countries)
    education=st.selectbox("Education",education)

    
    years_of_experience=st.number_input("Years of experience in the industry (years)")
    
    ok=st.button("Calculate Salary")

    if ok:
        X=np.array([[country,education,years_of_experience]])
        X[:,0]=le_country.transform(X[:,0])
        X[:,1]=le_education.transform(X[:,1])
        X=X.astype(float)

        salary=reg_model.predict(X)

        st.subheader(f"The estimated salary is ${salary[0]:.2f}")

