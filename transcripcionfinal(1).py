#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 18:32:45 2022

@author: kala
"""


import speech_recognition as sr
import ffmpeg

apt install ffmpeg
pip install pydub


# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import aspose.words as aw

# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    sound = AudioSegment.from_wav(path)  

    chunks = split_on_silence(sound,

        min_silence_len = 500,

        silence_thresh = sound.dBFS-14,

        keep_silence=500,
    )
    folder_name = "audio-chunks"

    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""

    for i, audio_chunk in enumerate(chunks, start=1):

        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")

        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)

            try:
                text = r.recognize_google(audio_listened, language= "es-ES")
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                whole_text += text       

    return whole_text


#documento a transcribir
    
clase_13 = "CLASE_13.wav"


doc = aw.Document()

builder = aw.DocumentBuilder(doc)

builder.write(get_large_audio_transcription(clase_13))
doc.save("clase13.docx")
    