import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Marvellous Infosystem Dashboard")

st.title("Marvellous infosystems")
st.header("Coustomer Churn Prediction")
st.write("Machine learning application Dashboard")

model=joblib.load("Marvellous_churn.pkl")

st.subheader("Enter customer details")

Age=st.number_input("Customer Age",min_value=1)
Tenure=st.number_input("Tenure (months)",min_value=0)
MonthlyCharges=st.number_input("Monthly Charges",min_value=0)
SupportCalls=st.number_input("Support calls",min_value=0)

if st.button("Button churn"):
    new_customer=pd.DataFrame({
    "Age":[Age],
    "Tenure":[Tenure],
    "MonthlyCharges":[MonthlyCharges],
    "SupportCalls":[SupportCalls]
    })

    prediction=model.predict(new_customer)

    if prediction==1:
        st.error("Coustomer is likely to churn")
    else:
        st.success("Coustomer is unlikely to churn")

st.divider()

st.caption("Marvellous Infosystem Dashboard")

