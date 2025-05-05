import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.title("AtliQ T Shirts: Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    result = chain.invoke(question)

    st.header("Answer")
    st.write(result['result'])