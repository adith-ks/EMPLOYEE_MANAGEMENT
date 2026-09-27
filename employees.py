import streamlit as st
from employee import Employee_manager

employees_instance = Employee_manager()
tab1,tab2 = st.tabs(["ADD","VIEW"])

with tab1:
    st.title("Add new employee")
    # name, place, mobile, email, departement, salary, joining_date)
    name = st.text_input("Enter the name")
    place = st.text_input("Enter the place")
    mobile=st.text_input("Enter the mobile number")
    email=st.text_input("Enter the email")
    departement=st.text_input("Enter the depsrtement")