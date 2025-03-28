import streamlit as st
import urllib.parse

def gerar_url_login():
    client_id = st.secrets["suap"]["client_id"]
    redirect_uri = st.secrets["suap"]["redirect_uri"]
    auth_host = st.secrets["suap"]["auth_host"]
    scope = st.secrets["suap"]["scope"]

    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "token",  
        "scope": scope
    }

    url = f"{auth_host}/o/authorize/?{urllib.parse.urlencode(params)}"
    return url
