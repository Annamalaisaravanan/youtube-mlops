import streamlit as st


st.title('Streamlit secrets management')


st.write("user: ",st.secrets['db_username'])

st.write("pass: ",st.secrets['db_password'])



st.write(st.secrets.cred.cred1,st.secrets.cred['cred2'])