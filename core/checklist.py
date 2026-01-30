import streamlit as st
import pandas as pd

def checklist_view():
st.title("CHECKLIST DO PROJETO")
checklist = pd.read_csv("data/checklist.csv")
st.dataframe(checklist)
