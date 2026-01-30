import streamlit as st
import pandas as pd
from core.indicadores import indice_maturidade


def projeto_view():
    st.title("RAIO X DO PROJETO")

    projetos = pd.read_csv("data/projetos.csv")
    checklist = pd.read_csv("data/checklist.csv")

    projeto_nome = st.selectbox("Selecione o projeto", projetos['nome'])
    projeto = projetos[projetos['nome'] == projeto_nome].iloc[0]

    st.subheader(f"Projeto: {projeto_nome}")
    st.write(f"Fase: {projeto['fase']}")
    st.write(f"Responsável: {projeto['responsavel']}")

    dados = checklist[checklist['projeto_id'] == projeto['id']]
    maturidade = indice_maturidade(dados.to_dict("records"))

    st.metric("ÍNDICE DE MATURIDADE", f"{maturidade}%")
    st.dataframe(dados)
