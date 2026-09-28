from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Super Dr. Raphael", page_icon="🦷", layout="centered")

# Esconde menu, cabeçalho e rodapé do Streamlit e reduz margens
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0.5rem 0.5rem 0 0.5rem; max-width: 1000px;}
      [data-testid="stAppViewContainer"] {background: #12308f;}
    </style>
    """,
    unsafe_allow_html=True,
)

html = Path(__file__).parent.joinpath("super-dr-raphael.html").read_text(encoding="utf-8")
components.html(html, height=920, scrolling=True)
