#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:35:36 2022

@author: rodrigoborneo
"""

import datetime
from pytube import YouTube


def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = video.filesize
    size = contentsize - bytes_remaining
    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')


url = input("Digite a URL do vídeo: ")
yt = YouTube(url, on_progress_callback=progress)


#Título do video
print("Título: ",yt.title)

#Visualizações video
print("Número de views: ",yt.views)

#Comprimento do video em segundos
#print("Length of video: ",yt.length,"seconds")

#comprimento do vídeo em horas minutos e segundos
converte_tempo = str(datetime.timedelta(seconds=yt.length))
print("Duração do video: ",converte_tempo)

#Data de publicação do vídeo
print("Data de publicação: ",yt.publish_date)

#Descrição do video(caso queira, apagar o #)
#print("Description:\n",yt.description)

#Pega a url da imagem da thumbnail
print("Thumbnail: ", yt.thumbnail_url)

video = yt.streams.get_highest_resolution()
print(yt.streams.get_highest_resolution().resolution)
video.download()

def audio_download():
    print("Fazendo o download apenas do audio do vídeo")
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()
    
