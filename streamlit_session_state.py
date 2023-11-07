import streamlit as st


st.title('Streamlit session state')



st.session_state['a_counter'] = 0

st.session_state.boolean = False

for the_values in st.session_state.values():
      st.write(the_values)



for the_values in st.session_state.keys():
      st.write(the_values)    

for the_values in st.session_state.items():
      st.write(the_values) 


slider = st.slider("my slider",0,10)

st.session_state.a_counter = slider

st.session_state

st.write('The value of the slider is ',st.session_state.a_counter)




   
