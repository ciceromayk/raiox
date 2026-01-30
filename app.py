import streamlit as st
from ui.dashboard import dashboard_view
from ui.projeto import projeto_view


st.set_page_config(page_title="RAIO X DE PROJETOS", layout="wide")


st.sidebar.title("RAIO X DE PROJETOS")
menu = st.sidebar.radio("MENU", ["Dashboard", "Projeto"])


if menu == "Dashboard":
dashboard_view()
elif menu == "Projeto":
projeto_view()
