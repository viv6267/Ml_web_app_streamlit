import streamlit as st

from predict_page import show_predict_page
from explore_page import show_explore_page

option=st.sidebar.selectbox("Explore or Predict", ("predict", "Explore"))#,"Survey_Details"))

if option=="predict":
    show_predict_page()
elif option=="Explore":
    show_explore_page()
else:
    st.link_button("Survey Details", "https://survey.stackoverflow.co/2024")
