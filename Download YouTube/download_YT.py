#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:35:36 2022

@author: rodrigoborneo
"""

import datetime
from pytube import YouTube
from pytube.cli import on_progress

url = input("Digite a URL do vídeo: ")
yt = YouTube(url, on_progress_callback=on_progress)

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



res=input("Deseja baixar audio ou video? ")

if (res=="video"):
    video = yt.streams.get_highest_resolution()
    print(yt.streams.get_highest_resolution().resolution)
    video.download()
    
    print("\nDownload do vídeo concluído\n")

if(res=="audio"):
    print("Fazendo o download apenas do audio do vídeo")
    audio = yt.streams.filter(only_audio=True)[0]
    audio.download()
    print("\nDownload do audio concluído\n")
    
