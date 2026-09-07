import streamlit as st
from src.agents import run_crew
st.title("Agentic RAG Assistant")
q=st.text_input("Ask a question")
if st.button("Submit") and q:
    st.write(run_crew(q))
