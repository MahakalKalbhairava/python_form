import streamlit as st
import pandas as pd
#st.title("Welcome to Hell")
#st.header("Python")
#st.subheader("Java")
#st.markdown("I love python")# to add text
#st.code(""" for i in range(1,5,1):
        #print(Hello world) """)# to add code
name=st.text_input("Enter your name :")
fname=st.text_input("Enter your father name :")
adr=st.text_area("Enter your text :")#to create large area to fit text
classdata=st.selectbox("Enter your class :",(1,2,3,4,5,6))
button=st.button("Done")#created done button
if button:
    st.markdown(f"""Name:{name}
                    Father name:{fname}
                    Address:{adr}    
                    Classdata:{classdata}    """)



