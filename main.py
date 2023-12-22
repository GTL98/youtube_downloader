# --- Importar as bibliotecas --- #
import os
import tkinter as tk
from PIL import Image
import streamlit as st
from pytube import YouTube
from tkinter import filedialog
from downloader import downloader

if os.environ.get('DISPLAY', '') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')

# --- Configurar o Tkinter --- #
root = tk.Tk()
root.withdraw()

# --- O seletor de pastas ficará sobre todas as janelas --- #
root.wm_attributes('-topmost', 1)

# --- Configuração da páginas --- #
icone = Image.open('./imagens/logo.png')
st.set_page_config(page_title='YouTube Downloader', page_icon=icone)

with st.container():
    # --- Título da página --- #
    st.title('YouTube Downloader')

with st.container():
    # --- Link do vídeo --- #
    link = st.text_input(label='Link:', placeholder='Link do vídeo')

    # --- Vídeo ou áudio --- #
    escolha = st.radio(
        'Escolha uma das opções:',
        (
            'Vídeo',
            'Áudio'
        ),
        horizontal=True
    )

    # --- Criar colunas para colocar o título e a thumb do vídeo --- #
    col_1, col_2 = st.columns((1, 2))

    # --- Iniciar a classe --- #
    if link != '':
        yt = YouTube(link)

        # --- Título do vídeo --- #
        with col_1:
            st.subheader(yt.title)

        # --- Thumb do vídeo --- #
        with col_2:
            st.image(yt.thumbnail_url)

        # --- Botão para fazer o download --- #
        with st.container():
            # --- Baixar a mídia --- #
            col_1, col_2, col_3, col_4, col_5 = st.columns(5)
            with col_3:
                baixar = st.button('Baixar')
            if baixar:
                caminho = filedialog.askdirectory(master=root)  # seleciona a pasta de destino do arquivo
                downloader(escolha, link, caminho)
