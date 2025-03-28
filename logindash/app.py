import streamlit as st
from login_suap import gerar_url_login

# Estilo com fundo verde pastel e botão centralizado
st.markdown(
    """
    <style>
    body {
        background-color: #d8f3dc;
    }
    .titulo {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        color: #1b4332;
        margin-bottom: 30px;
    }
    .btn-suap {
        display: block;
        margin: 0 auto;
        background-color: #95d5b2;
        color: black;
        font-weight: bold;
        font-size: 1.2em;
        padding: 0.6em 2em;
        border: none;
        border-radius: 10px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .btn-suap:hover {
        background-color: #74c69d;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="titulo">Sistema de Controle de Alarmes - IFRO</div>', unsafe_allow_html=True)

# Gera a URL de login com os dados do st.secrets
login_url = gerar_url_login()

st.markdown(
    f'<a href="{login_url}"><button class="btn-suap">Entrar via SUAP</button></a>',
    unsafe_allow_html=True
)
