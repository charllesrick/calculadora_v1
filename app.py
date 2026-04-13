import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

st.markdown("""
<style>
    .stApp { background: #1a1a2e; }
    #MainMenu, footer, header {visibility: hidden;}
    .block-container {padding: 0 !important;}
    iframe { border: none; }
</style>
""", unsafe_allow_html=True)

with open("calculadora.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=700, scrolling=False)