import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
def project_board():
    data = pd.read_csv('D:\EVA\DS\GIT_Porto\Portofolio-Streamlit\employee_survey_fin.csv')
    st.subheader('Employee Data Set')
    st.write(data.head(10))
    st.markdown("## Employee Dashboard")
    
    employee_number = pd.DataFrame(data['gender'].value_counts())
    satisfication = pd.DataFrame(data['satisfaction_category'].value_counts())
    department_satisfaction = data[data['satisfaction_category'] == 'Satisfied'].groupby('dept').size().reset_index(name='count')

    st.button("Reset", type="primary")

    if st.button("Number Of Employee"):
        st.write(employee_number)
        st.bar_chart(employee_number)
    
    if st.button("satisfication rate"):
        st.bar_chart(satisfication)

     
    if st.button("Department satisfacion rate"):
        fig = px.pie(department_satisfaction, values='count', names='dept', title='Department Satisfaction',
                    color_discrete_sequence=px.colors.qualitative.Set1, hole=0.3)

        st.plotly_chart(fig)