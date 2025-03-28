import streamlit as st
from login_suap import gerar_url_login

def show_login_screen():
   
    st.markdown(
        """
        <style>
        body {
            background-color: #d8f3dc;
        }
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .titulo {
            font-size: 2.5em;
            font-weight: bold;
            color: #1b4332;
            margin-bottom: 20px;
            text-align: center;
        }
        .descricao {
            font-size: 1.1em;
            color: #2d6a4f;
            text-align: center;
            max-width: 500px;
            margin-bottom: 40px;
        }
        .btn-suap {
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
        <div class="container">
            <div class="titulo">Dashboard - IFRO</div>
            <div class="descricao">
                Bem-vindo(a) ao dashboard para análise de desempenho acadêmico do IFRO.
                Para continuar, faça login via SUAP.
            </div>
        """,
        unsafe_allow_html=True
    )

    login_url = gerar_url_login()
    st.markdown(
        f'<a href="{login_url}"><button class="btn-suap">Entrar via SUAP</button></a>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

def show_logged_in_screen():
   
    st.markdown(
        """
        <style>
        body {
            background-color: #d8f3dc;
        }
        .welcome-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .welcome-title {
            font-size: 2em;
            font-weight: bold;
            color: #1b4332;
            margin-bottom: 20px;
            text-align: center;
        }
        .logout-btn {
            background-color: #95d5b2;
            color: black;
            font-weight: bold;
            font-size: 1em;
            padding: 0.5em 1.5em;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .logout-btn:hover {
            background-color: #74c69d;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="welcome-container">', unsafe_allow_html=True)
    st.markdown('<div class="welcome-title">Você está logado, bem-vindo(a)</div>', unsafe_allow_html=True)

    if st.button("Sair"):
       
        st.experimental_set_query_params(access_token=None)
        st.experimental_rerun()

    st.markdown("</div>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Dash IFRO", layout="wide")


    query_params = st.query_params
    token = query_params.get("access_token", [None])[0]

    if token:
        show_logged_in_screen()
    else:
        show_login_screen()

if __name__ == "__main__":
    main()
