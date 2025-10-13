import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Gerenciador de livros", page_icon="🎬")
st.title("📽 Gerenciador de Filmes 🎞")

menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar filme", "Exibir filmes", ])

if menu == "Catalogo":
    st.subheader("Todos os filmes disponiveis")
    response = requests.get(f"{API_URL}/listar_filmes")
    if response.status_code == 200:
        filmes = response.json().get("filmes", [])
        if filmes:
            for linha in filmes:
                st.write(f"**{linha['id']}** ")
    
    else:
        st.error("Erro ao acessar a API")