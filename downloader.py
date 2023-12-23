# --- Importar a biblioteca --- #
import os
import streamlit as st
from pytube import YouTube


def downloader(tipo: str, link: str):
    """
    Função responsável por retornar a mídia do vídeo baixado.
    :param tipo: 'Vídeo' ou 'Áudio'.
    :param link: Link do vídeo.
    """
    if tipo == 'Áudio':
        # --- Inicializar a classe --- #
        yt = YouTube(link)

        # --- Armazenar a inforação do vídeo na variável --- #
        audio = yt.streams.filter(only_audio=True).first()

        # --- Armazenar a saída da mídia --- #
        saida = audio.download()

        # --- Converter para MP3 --- #
        base, ext = os.path.splitext(saida)
        novo_arquivo = base + '.mp3'
        os.rename(saida, novo_arquivo)

        # --- Informar que o download foi concluído --- #
        st.subheader('Download concluído!')

    if tipo == 'Vídeo':
        # --- Inicializar a classe --- #
        yt = YouTube(link)

        # --- Armazenar a inforação do vídeo na variável --- #
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()

        # --- Armazenar a saída da mídia --- #
        video.download()

        # --- Informar que o download foi concluído --- #
        st.subheader('Download concluído!')
