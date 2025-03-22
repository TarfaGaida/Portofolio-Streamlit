import streamlit as st

st.set_page_config(layout='wide')
st.title('My Portofolio')
st.header('Data Science')

st.sidebar.title('Navigation')

page = st.sidebar.radio('Choose page', ['about me','Dashboard', "Contact"])

if page =='about me':
    import about
    about.about_me()

elif page =='Contact':
    import contact
    contact.show_contact()

elif page == 'Dashboard':
    import project
    project.project_board()