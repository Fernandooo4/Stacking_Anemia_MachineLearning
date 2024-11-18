import streamlit as st
import pandas as pd
import joblib  # Para cargar el modelo guardado
import pickle
from PIL import Image


# Función para cargar el archivo CSS de fondo
with open("assets/fondo_acerca.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([5.3, 4], gap="small", vertical_alignment="center")


with col1:
    st.markdown("""
    <style>
        /* Modificar la tipografía del título con efecto llamativo */
        .title {
            font-family: 'Bahnschrift SemiBold', 'Times New Roman', sans-serif; 
            font-size: 180px; /* Tamaño del título */
            color: #FF5722; /* Naranja brillante */
            text-align: left; /* Centrar el título */
            margin-top: 1px; /* Mover el título un poco más arriba */
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite; /* Animación */
        }

        /* Efecto de cambio de color en el título */
        @keyframes colorChange {
            0% { color: #FF5722; } /* Naranja brillante */
            50% { color: #D84315; } /* Naranja más oscuro */
            100% { color: #FF5722; } /* Naranja brillante */
        }

        /* Efecto de sombra en el título */
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title">MACHINE</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
        .title3 {
            font-family: 'Bahnschrift SemiBold', 'Times New Roman', sans-serif; 
            font-size: 180px;
            color: #FF5722;
            text-align: left;
            margin-top: -140px;
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite;
        }
        @keyframes colorChange {
            0% { color: #FF5722; }
            50% { color: #D84315; }
            100% { color: #FF5722; }
        }
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title3">LEARNING</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
        .title2 {
            font-family: 'Bahnschrift SemiBold', 'Times New Roman', sans-serif;
            font-size: 86px;
            color: #FF5722;
            text-align: left;
            margin-top: -95px;
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite;
        }
        @keyframes colorChange {
            0% { color: #FF5722; }
            50% { color: #D84315; }
            100% { color: #FF5722; }
        }
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title2">EN LA DETECCIÓN</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
        .title4 {
            font-family: 'Bahnschrift SemiBold', 'Times New Roman', sans-serif;
            font-size: 90px;
            color: #FF5722;
            text-align: leftt;
            margin-top: -64px;
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite;
        }
        @keyframes colorChange {
            0% { color: #FF5722; }
            50% { color: #D84315; }
            100% { color: #FF5722; }
        }
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title4">DE LA</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
        .title5 {
            font-family: 'Bahnschrift SemiBold', 'Times New Roman', sans-serif;
            font-size: 210px;
            color: #FF5722;
            text-align: left;
            margin-top: -105px;
            animation: colorChange 3s infinite, shadowEffect 3s ease-in-out infinite;
        }
        @keyframes colorChange {
            0% { color: #FF5722; }
            50% { color: #D84315; }
            100% { color: #FF5722; }
        }
        @keyframes shadowEffect {
            0% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
            50% { text-shadow: 0 0 10px rgba(0, 0, 0, 0.5), 0 0 20px rgba(0, 0, 0, 0.3); }
            100% { text-shadow: 0 0 5px rgba(0, 0, 0, 0.5), 0 0 10px rgba(0, 0, 0, 0.3); }
        }
    </style>
    <div class="title5">ANEMIA</div>
    """, unsafe_allow_html=True)

with col2:
    st.image("imagenes/gotin.png", width = 685)






col3, col4, col5= st.columns([1,5, 1], gap="small", vertical_alignment="center")

with col4:
    st.image("imagenes/que.png", width = 800)


col6, col7 = st.columns([10,17], gap="small", vertical_alignment="center")
with col6:
    st.image("imagenes/vaso.png", width = 460)
with col7:
    st.image("imagenes/txt.png", width= 510)


col8, col9, col10= st.columns([1,5, 1], gap="small", vertical_alignment="center")

with col9:
    st.image("imagenes/ga.png", width = 1000)


col11, col12, col13 = st.columns([6.2,17.1,13], gap="small", vertical_alignment="center")

with col12:
    st.image("imagenes/sn.png", width = 470)
with col13:
    st.image("imagenes/Q.png", width = 220)


col14, col15 = st.columns([10,17], gap="small", vertical_alignment="center")
with col14:
    st.image("imagenes/es.png", width = 620)
with col15:
    st.image("imagenes/robot.png", width= 670)


col16, col17, col18 = st.columns([3,3,3], gap="small", vertical_alignment="center")

with col17:
    st.image("imagenes/gas.png", width = 1300)
