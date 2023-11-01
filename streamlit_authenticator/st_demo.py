import streamlit as st
import pandas as pd
import sqlite3
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

import streamlit_authenticator as stauth

import yaml
from yaml.loader import SafeLoader


with open('config.yml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

authentication_status = authenticator.login('SQL DB Login', 'main')


if st.session_state["authentication_status"] == False:
       st.error("Username/password is incorrect")

elif st.session_state["authentication_status"] == None:
       st.warning("Please enter your username and password")

elif st.session_state["authentication_status"] == True:

               st.title('Streamlit App with SQLite3')


               page = st.sidebar.selectbox("pages",["sql injection","sql table viewer"])
               
               

               if page =="sql injection":
                    st.write("This is to inject iris data to the sql database")

                    
                    sepal_length = st.number_input('Insert sepal length number')
                    sepal_width = st.number_input('Insert sepal width number')
                    petal_length= st.number_input('Insert petal length number')
                    petal_width = st.number_input('Insert petal width number')
                    
                    species = st.selectbox(
               'species',
               ('setosa', 'virginia', 'versicolor'))
                    
                    submit = st.button("submit")

                    if submit:
                                   # Connect to the SQLite database (it will create a new database if it doesn't exist)
                                   conn = sqlite3.connect(r'C:\Users\Annamalai\Downloads\Youtube-contents\deep_matrix.db')

                                   # Create a cursor object to interact with the database
                                   cursor = conn.cursor()

                                   cursor.execute("INSERT INTO iris (sepal_length, sepal_width, petal_length, petal_width, species) VALUES (?, ?, ?, ?, ?)",
                              (sepal_length, sepal_width, petal_length, petal_width, species))
                                   
                                   conn.commit()
                                   conn.close()

                    

                    

               else:
                    

                    conn = sqlite3.connect(r'C:\Users\Annamalai\Downloads\Youtube-contents\deep_matrix.db')
                    cursor = conn.cursor()
                    g = cursor.execute('select * from iris')
                    data = g.fetchall()

                    columns = [desc[0] for desc in cursor.description]

                         # Create a Pandas DataFrame from the fetched data and column names
                    df = pd.DataFrame(data, columns=columns)

                    st.dataframe(df)
               authenticator.logout('Logout', 'main', key='unique_key')




         
      


      







     
