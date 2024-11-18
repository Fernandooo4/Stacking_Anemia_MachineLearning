import streamlit as st
import pandas as pd
import joblib  # Para cargar el modelo guardado


st.set_page_config(page_title="Deteccion de anemia", page_icon="🔬", layout="wide")
# Función para cargar el archivo CSS de fondo
with open("assets/fondo_principal.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Título y descripción de la aplicación




import streamlit as st

# HTML y CSS para personalizar el título
st.sidebar.markdown("""
    <style>
        .big-title {
            font-size: 40px;
            font-family: 'Mongolian Baiti', Mongolian Baiti;
            color: black;
            text-align: center;
            font-weight: bold;
        }
    </style>
    <div class="big-title"></div>
""", unsafe_allow_html=True)

# Agregar una imagen debajo del título
st.sidebar.image("imagenes/logo.png", use_column_width=True)

# ---PAGE SETUP --
project_3_page = st.Page(
    page = "pages/MlAnemia.py",
    title = "Inicio 🙋🏻‍♂️",
    icon = ":material/quiz:",
    default = True,
)
about_page = st.Page(
    page = "pages/Prediccion.py",
    title = "Predicción 🩸",
    icon = ":material/bloodtype:",
)
project_1_page = st.Page(
    page = "pages/Subir_archivo_CSV.py",
    title = "Subir archivo CSV 🗂️",
    icon = ":material/description:",
)
project_2_page = st.Page(
    page = "pages/FAQ.py",
    title = "Preguntas ❓",
    icon = ":material/contact_support:",
)

# Menu navegación
pg = st.navigation(pages=[project_3_page, about_page, project_1_page, project_2_page])

# Run navegación
pg.run()
