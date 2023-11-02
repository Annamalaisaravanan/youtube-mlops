import streamlit as st


st.title('Streamlit layers and containers')

tab1, tab2, tab3, tab4 = st.tabs(["Cat", "Dog", "Owl",'Lion'])

with tab1:
   st.header("This is tab 1")
   
with tab2:
   st.header("This is tab 2")
   
with tab3:
   st.header("This is tab 3")


col1, col2, col3 = st.columns(3)

with col1:
    b1 =st.button("submit")

b2 =st.sidebar.button("login")

b2 =st.sidebar.button("logout")


with st.expander('open me'):
       st.image("https://static.streamlit.io/examples/dice.jpg")

    





   
