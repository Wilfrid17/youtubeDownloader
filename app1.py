import streamlit as st
from yt_dlp import YoutubeDL  # Corrigido aqui
import os

# Configurando o título do app no Streamlit
st.title("YouTube Downloader")

# Exemplo de uso do yt_dlp
link = st.text_input("Insira o link do vídeo do YouTube")

if st.button("Baixar"):
    if link:
        yt_opts = {
            'format': 'best',#Garante que abaixo video e áudio
            'outtmpl': '%(title)s.%(ext)s',
        }

        with YoutubeDL(yt_opts) as ydl:  # Corrigido aqui
            ydl.download([link])
        st.success("Download concluído!")
    else:
        st.error("Por favor, insira um link válido.")
