# --- Importar as bibliotecas --- #
import os
import winreg
import streamlit as st
from pytube import YouTube

# --- Caminho da pasta download --- #
reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")
pasta_download = winreg.QueryValueEx(reg_key, "{374DE290-123F-4565-9164-39C4925E467B}")[0]
winreg.CloseKey(reg_key)
CAMINHO = pasta_download.replace('\\', '/')


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
        saida = audio.download(CAMINHO)

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
        video.download(CAMINHO)

        # --- Informar que o download foi concluído --- #
        st.subheader('Download concluído!')
