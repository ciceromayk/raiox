import streamlit as st
import pandas as pd
from core.indicadores import indice_maturidade

def dashboard_view():
st.title("DASHBOARD GERENCIAL")
projetos = pd.read_csv("data/projetos.csv")
checklist = pd.read_csv("data/checklist.csv")
col1, col2, col3 = st.columns(3)
col1.metric("TOTAL DE PROJETOS", len(projetos))
maturidade = indice_maturidade(checklist.to_dict("records"))
col2.metric("MATURIDADE MÉDIA", f"{maturidade}%")
atrasados = checklist[checklist['status'] == 'Atrasado']
col3.metric("ITENS EM RISCO", len(atrasados))
st.dataframe(projetos)
